# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20170601_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovation',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='innovation',
            name='updatedtime',
            field=models.DateField(auto_now=True),
        ),
    ]
