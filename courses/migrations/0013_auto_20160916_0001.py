# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='End of Subject Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='init_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Begin of Subject Date'),
            preserve_default=False,
        ),
    ]
