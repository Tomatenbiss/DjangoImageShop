from django.http import HttpResponse
from django.shortcuts import render

from carton.cart import Cart
from photos.models import Photo


def add(request):
    cart = Cart(request.session)
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
