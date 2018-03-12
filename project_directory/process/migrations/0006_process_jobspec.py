# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-06 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobspec', '0001_initial'),
        ('process', '0005_remove_process_jobsepc'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='jobspec',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobspec.JobSpec'),
        ),
    ]