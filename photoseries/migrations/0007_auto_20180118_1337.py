# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 13:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoseries', '0006_auto_20180116_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photoseries',
            old_name='description',
            new_name='describtion',
        ),
    ]