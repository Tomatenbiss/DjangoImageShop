# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.


def start_view(request):
    context = {}
    return render(request, 'accounts/landingpage.html', context)


def login_view(request):
    context = {}
    return render(request, 'accounts/login.html', context)


def profile(request):
    context = {}
    return render(request, 'accounts/profile.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('start_view')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registration.html', {'form': form})

