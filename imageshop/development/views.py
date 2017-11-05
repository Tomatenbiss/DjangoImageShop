# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def start_view(request):
    context = {}
    return render(request, 'development/landingpage.html', context)


def registration(request):
    context = {}
    return render(request, 'development/registration.html', context)


def login(request):
    context = {}
    return render(request, 'development/login.html', context)