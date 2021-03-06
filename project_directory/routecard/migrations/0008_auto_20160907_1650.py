# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-07 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routecard', '0007_auto_20160906_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='routecardreport',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='routecard.Plan'),
        ),
        migrations.AlterField(
            model_name='routecard',
            name='jobspec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobspec.JobSpec'),
        ),
    ]
