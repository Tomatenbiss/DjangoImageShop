from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import auth

from carton.cart import Cart

from imageshop import settings
from photos.models import Photo
from photoseries.models import Photoseries
from orders.models import Order

from django.core.exceptions import SuspiciousOperation

def add(request):
    cart = Cart(request.session)
    try:
        photseries = Photoseries.objects.get(id=request.GET.get('id'))
        photss = photseries.images.all()
        iterations = 0
        for phots in photss:
           if iterations == 0:
              if phots in cart.products:
                 if request.user == phots.owner:
                     return HttpResponse("You can not buy your own photoseries. Sorry.")
                 else:
                     cart.remove(phots)
                     cart.add(phots, price=photseries.price)
                     iterations += 1
              else:
                 if request.user == phots.owner:
                     return HttpResponse("You can not buy your own photoseries. Sorry.")
                 else:
                     cart.add(phots, price=photseries.price)
                     iterations += 1
           else:
              if request.user == phots.owner:
                  return HttpResponse("You can not buy your own photoseries. Sorry.")
              else:
                  cart.add(phots, 0.0)
        return render(request, 'carts/redirect.html')
    except:
        phot = Photo.objects.get(id=request.GET.get('id'))
        if phot in cart.products:
            return HttpResponse("Photo already in shopping cart")
        else:
            if request.user == phot.owner:
                return HttpResponse("You can not buy your own photos. Sorry.")
            else:
                cart.add(phot, price=phot.price)
                return render(request, 'carts/redirect.html')

def remove(request):
    cart = Cart(request.session)
    phot = Photo.objects.get(id=request.GET.get('id'))
    cart.remove(phot)
    return render(request, 'carts/redirect.html')

def clear(request):
    cart = Cart(request.session)
    cart.clear()
    return render(request, 'carts/redirect.html')


def show(request):
    return render(request, 'carts/show-cart.html')

class checkoutView(TemplateView):
    template_name = "carts/checkout.html"

    def get_context_data(self, **kwargs):
        '''Hooks into request lifecycle and processes the order'''
        # Get cart from the current session
        cart = Cart(self.request.session)
        if not cart.products:
            raise SuspiciousOperation("Cart is empty")
        # Split cart by photo/photoseries owner
        sellers_photo_dict = self.__split_by_owner(cart.products)
        # Create order for each author
        orders = []
        for seller, photo_list in sellers_photo_dict.items():
            order = Order()
            order.buyer = auth.get_user(self.request)
            order.seller = seller
            order.save()
            for photo in photo_list:
                # Delete key to save a new photo instance to the database
                photo.pk = None
                photo.order_copy = True
                photo.save()
                order.photos.add(photo)
            orders.append(order)
        # 4. Versende für jede Order zwei Mails
          # 4.1 Bestätigungsmail
            buyer = User.objects.get(id=order.buyer_id)
            send_mail(
                'Order Confirmation',
                'Your order was confirmed. The owner will contact you for the payment.',
                settings.EMAIL_HOST_USER,
                [buyer.email],
                fail_silently=True,
                auth_user=settings.EMAIL_HOST_USER,
                auth_password=settings.EMAIL_HOST_PASSWORD
            )
          # 4.2 Mail mit Info für den Verkäufer
            send_mail(
                'New Order',
                'You got a new order. Please login to accept the incoming order',
                settings.EMAIL_HOST_USER,
                [order.seller.email],
                fail_silently=True,
                auth_user=settings.EMAIL_HOST_USER,
                auth_password=settings.EMAIL_HOST_PASSWORD
            )
        # Show success message to user
        context = super(checkoutView, self).get_context_data(**kwargs)
        context['orders'] = orders
        cart.clear()
        return context

    def __split_by_owner(self, list_to_split):
        # dict format: {owner1: [obj1, obj2, ...], ...}
        owner_object_list_dict = {}
        for obj in list_to_split:
            if (owner_object_list_dict.get(obj.owner)):
                owner_object_list_dict.get(obj.owner).append(obj)
            else:
                owner_object_list_dict[obj.owner] = [obj]
        return owner_object_list_dict
