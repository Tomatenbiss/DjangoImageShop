# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-23 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicLink', '__first__'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='downloads',
            field=models.ManyToManyField(to='dynamicLink.Download'),
        ),
    ]
