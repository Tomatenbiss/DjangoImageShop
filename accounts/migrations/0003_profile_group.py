# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20171114_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='group',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]