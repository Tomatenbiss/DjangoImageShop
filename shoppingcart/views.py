from django.http import HttpResponse
from django.shortcuts import render

#def add(request):

def registration(request):
    return render(request, 'shoppingcart/show-cart.html')

def show(request):
    return render(request, 'shoppingcart/show-cart.html')
