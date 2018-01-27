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

from django.core.exceptions import ObjectDoesNotExist, SuspiciousOperation

def __get_product_from_request(request):
    product_type = request.GET.get('product')
    if product_type != 'photo' and product_type != 'photoseries':
        raise SuspiciousOperation("Unknown product type!")
    try:
        if product_type == 'photo':
            return Photo.objects.get(id=request.GET.get('id'))
        else:
            return Photoseries.objects.get(id=request.GET.get('id'))
    except ObjectDoesNotExist:
        raise SuspiciousOperation(
            "Photo or photoseries with this key does not exist")

def add(request):
    cart = Cart(request.session)
    product = __get_product_from_request(request)
    if product in cart.products:
        raise SuspiciousOperation("Photo already in shopping cart")
    if product.owner == request.user:
        raise SuspiciousOperation("You can not buy your own photos")
    cart.add(product, price=product.price)
    
    return render(request, 'carts/redirect.html')


def remove(request):
    cart = Cart(request.session)
    product = __get_product_from_request(request)
    cart.remove(product)
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
        # Create order for each author
        orders = []
        for product in cart.products:
            # Save new instance of product to the database
            product.order_copy = True
            # Backup reference to images from photoseries
            if isinstance(product, Photoseries):
                original_images = product.images.all()
            product.pk = None
            product.save()
            # Set reference to images again
            if isinstance(product, Photoseries):
                product.images.set(original_images)
                product.save()
            # Check if order for seller exists
            existing_order = [order for order in orders if order.seller == product.owner]
            if len(existing_order) != 1:
                order = Order()
                order.buyer = auth.get_user(self.request)
                order.seller = product.owner
                orders.append(order)
                order.save()
            else:
                order = existing_order[0]
            # Put product inside order
            if isinstance(product, Photo):
                order.photos.add(product)
            else:
                order.photoseries.add(product)
            order.save()
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
