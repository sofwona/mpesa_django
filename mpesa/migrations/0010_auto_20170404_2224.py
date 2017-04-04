# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-04 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0009_auto_20170404_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, default=3, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]