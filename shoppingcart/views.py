from django.http import HttpResponse
from django.shortcuts import render

from carton.cart import Cart
from photo.models import Photo

def add(request):
    cart = Cart(request.session)
    phot = Photo.objects.get(id=request.GET.get('id'))
    cart.add(phot, price=phot.price)
    return HttpResponse("Added")


def remove(request):
    cart = Cart(request.session)
    phot = Photo.objects.get(id=request.GET.get('id'))
    cart.remove(phot)
    return HttpResponse("Removed")

def clear(request):
    cart = Cart(request.session)
    cart.clear()
    return HttpResponse("Cleared")

def show(request):
    return render(request, 'shoppingcart/show-cart.html')
