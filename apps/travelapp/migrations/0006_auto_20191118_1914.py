# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-18 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_auto_20191118_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='users',
            field=models.ManyToManyField(related_name='travels', to='travelapp.user'),
        ),
    ]