# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def start_view(request):
    context = {}
    return render(request, 'accounts/landingpage.html', context)


def registration(request):
    context = {}
    return render(request, 'accounts/registration.html', context)


def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)