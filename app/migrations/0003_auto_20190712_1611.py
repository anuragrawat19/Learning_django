# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-12 10:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='Details',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]
