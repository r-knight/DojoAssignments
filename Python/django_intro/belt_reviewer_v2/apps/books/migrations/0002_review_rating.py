# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-22 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]