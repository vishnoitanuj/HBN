# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-07 12:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0054_networkmembers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NetworkMembers',
            new_name='NetworkMember',
        ),
    ]
