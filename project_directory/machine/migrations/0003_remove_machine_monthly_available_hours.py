# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-06 09:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0002_machine_monthly_available_hours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='monthly_available_hours',
        ),
    ]
