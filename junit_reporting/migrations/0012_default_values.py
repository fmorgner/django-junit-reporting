# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junit_reporting', '0011_JUnitReport_unique_build_per_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junitsuite',
            name='runtime',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='junitsuite',
            name='skipped',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='junittest',
            name='runtime',
            field=models.FloatField(default=0),
        ),
    ]