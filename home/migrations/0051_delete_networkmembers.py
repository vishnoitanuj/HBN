# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-06 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_networkmembers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NetworkMembers',
        ),
    ]
