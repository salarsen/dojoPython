# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 04:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0004_auto_20161129_2047'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='course',
            table='course',
        ),
        migrations.AlterModelTable(
            name='enrolled',
            table='enrolled',
        ),
    ]
