# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-05 04:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0002_machine_monthly_available_hours'),
        ('process', '0003_remove_process_machine'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='machine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='processes', to='machine.Machine'),
        ),
    ]
