# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-07 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobspec', '0001_initial'),
        ('process', '0006_process_jobspec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process',
            name='jobspec',
        ),
        migrations.RemoveField(
            model_name='process',
            name='machine',
        ),
        migrations.AddField(
            model_name='process',
            name='jobsepc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobspec.JobSpec'),
        ),
    ]
