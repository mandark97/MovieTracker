# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-10 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_tracker', '0002_auto_20171220_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]