# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 04:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_resource_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='link',
            new_name='url',
        ),
    ]