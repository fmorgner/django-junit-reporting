# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('junit_reporting', '0004_add_JUnitSuite'),
    ]

    operations = [
        migrations.CreateModel(
            name='JUnitTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('classname', models.CharField(max_length=512)),
                ('runtime', models.FloatField()),
                ('suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junit_reporting.JUnitSuite')),
            ],
        ),
    ]
