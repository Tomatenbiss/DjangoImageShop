# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 15:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20171229_1544'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfileImage',
        ),
    ]
