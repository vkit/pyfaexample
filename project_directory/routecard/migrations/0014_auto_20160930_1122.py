# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-30 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routecard', '0013_routecard_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routecard',
            name='number',
            field=models.IntegerField(),
        ),
    ]
