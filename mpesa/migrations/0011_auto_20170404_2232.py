# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-04 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0010_auto_20170404_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='transaction_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_id',
        ),
    ]
