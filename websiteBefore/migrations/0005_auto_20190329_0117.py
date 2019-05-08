#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
# Generated by Django 2.1.5 on 2019-03-29 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteBefore', '0004_auto_20190325_0209'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrickMessage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('companyName', models.CharField(max_length=20)),
                ('trickMoney', models.IntegerField()),
                ('tables_one', models.CharField(max_length=255)),
                ('tables_two', models.CharField(max_length=255)),
                ('tables_three', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'trickMessage',
            },
        ),
        migrations.AlterField(
            model_name='classsay',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='new_message',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
