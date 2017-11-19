# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm

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
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
           # if request.POST["is_photographer"]:
            is_photographer = request.POST.get('is_photographer', False)
            if is_photographer:
                user.groups.add(Group.objects.get(name='photographer'))
            else:
                user.groups.add(Group.objects.get(name='customer'))
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('start_view')
    else:
        form = SignUpForm()
    return render(request, 'accounts/registration.html', {'form': form})
