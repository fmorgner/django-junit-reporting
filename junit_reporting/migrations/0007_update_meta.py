# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 12:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('junit_reporting', '0006_add_JUnitProblem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='junitproblem',
            options={'verbose_name': 'JUnit Test Case Problem'},
        ),
        migrations.AlterModelOptions(
            name='junitreport',
            options={'verbose_name': 'JUnit Test Report'},
        ),
        migrations.AlterModelOptions(
            name='junitsuite',
            options={'verbose_name': 'JUnit Test Suite'},
        ),
        migrations.AlterModelOptions(
            name='junittest',
            options={'verbose_name': 'JUnit Test Case'},
        ),
    ]