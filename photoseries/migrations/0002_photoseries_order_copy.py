# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-27 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoseries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoseries',
            name='order_copy',
            field=models.BooleanField(default=False),
        ),
    ]
