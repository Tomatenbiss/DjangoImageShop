# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
def home(request):
    nums = [1,5,2,3]
    name = 'Max Muschdaman'

    args = {'name' : name, 'num' : nums}
    return render(request,'accounts/home.html', args)

def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/account')

    else:
        form = RegistrationForm()
        args = {'form' : form }
        return render(request, 'accounts/registration.html', args)


def profile(request):
    args ={'user' : request.user}
    return render(request, 'accounts/profile.html', args)