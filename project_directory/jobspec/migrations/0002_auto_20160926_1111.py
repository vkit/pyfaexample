# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-26 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobspec', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobspec',
            name='number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
