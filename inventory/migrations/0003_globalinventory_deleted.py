# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-13 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20191112_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalinventory',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
