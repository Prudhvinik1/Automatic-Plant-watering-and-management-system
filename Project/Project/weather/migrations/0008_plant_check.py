# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0007_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='check',
            field=models.CharField(default=100, max_length=8),
            preserve_default=False,
        ),
    ]
