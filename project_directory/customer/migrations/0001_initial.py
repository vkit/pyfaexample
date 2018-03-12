# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-02 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Contact Name')),
                ('company_name', models.CharField(max_length=50, unique=True, verbose_name='Company Name')),
                ('pan_no', models.CharField(blank=True, max_length=50, null=True)),
                ('tin_no', models.CharField(blank=True, max_length=50, null=True)),
                ('service_tax_no', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_terms', models.CharField(blank=True, max_length=100, null=True)),
                ('credit_days', models.IntegerField(default=0, verbose_name='Credit Period (Days)')),
                ('ph_number1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone No.')),
                ('ph_number2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Alternate No.')),
                ('addressline1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Addressline 1')),
                ('addressline2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Addressline 2')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-Mail')),
                ('zipcode', models.IntegerField(blank=True, null=True, verbose_name='Zipcode')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=100, null=True, verbose_name='State')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
