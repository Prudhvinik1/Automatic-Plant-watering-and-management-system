# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0010_auto_20171103_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantid',
            name='plant_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='moisture',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
