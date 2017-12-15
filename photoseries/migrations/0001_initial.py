# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_auto_20171215_2143'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photoseries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('describtion', models.CharField(max_length=100)),
                ('images', models.ManyToManyField(to='photos.Photo')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Photographer', verbose_name='Fotograf')),
            ],
        ),
    ]
