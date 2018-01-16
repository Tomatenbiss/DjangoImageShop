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
        for phots in photss:
            #print "object is a photoseries"
            if phots in cart.products:
               cart.remove(phots)
               cart.add(phots, price=photseries.price)
            else:
               cart.add(phots, price=photseries.price)
        return render(request, 'carts/redirect.html')
    except:
        phot = Photo.objects.get(id=request.GET.get('id'))
        if phot in cart.products:
            return HttpResponse("Photo already in shopping cart")
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
