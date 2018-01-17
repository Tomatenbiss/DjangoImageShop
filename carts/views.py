from django.http import HttpResponse
from django.shortcuts import render

from carton.cart import Cart
from photos.models import Photo
from photoseries.models import Photoseries

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
