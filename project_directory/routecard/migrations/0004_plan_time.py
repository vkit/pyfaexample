# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-06 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routecard', '0003_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]