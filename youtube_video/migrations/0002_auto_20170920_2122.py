# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-21 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ytvideo',
            name='url',
            field=models.CharField(max_length=250, verbose_name='URL'),
        ),
    ]
