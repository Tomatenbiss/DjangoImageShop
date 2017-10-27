# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Tag(models.Model):
    text = models.CharField(max_length=42, default='Tisch')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.text

    

    