# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-16 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_travel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='CPass',
        ),
    ]