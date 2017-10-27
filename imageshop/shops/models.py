# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from accounts.models import UserProfile
  

class Shop(models.Model):
    owner = models.OneToOneField(UserProfile)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.CharField(max_length=200, default='%s shop' % self.owner.UserProfile.user.username)

