# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 17:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20170823_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 14, 17, 30, 36, 819823, tzinfo=utc)),
        ),
    ]
