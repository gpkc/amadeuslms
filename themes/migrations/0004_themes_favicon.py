# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-12 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import themes.models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0003_auto_20170112_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='themes',
            name='favicon',
            field=models.ImageField(blank=True, default='favicon_amadeus.png', upload_to='themes/', validators=[themes.models.validate_img_extension], verbose_name='Favicon'),
        ),
    ]