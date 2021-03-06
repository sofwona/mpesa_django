# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-04 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0002_auto_20170404_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('identification', models.CharField(max_length=20)),
                ('phone_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='cost',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='user',
            name='transaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mpesa.Transaction'),
        ),
    ]
