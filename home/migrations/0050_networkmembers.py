# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-06 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_delete_network_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pic', models.FileField(upload_to='')),
            ],
        ),
    ]
