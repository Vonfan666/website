#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
# Generated by Django 2.1.5 on 2019-03-25 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteBefore', '0003_auto_20190325_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classsay',
            name='classSayImage',
            field=models.ImageField(upload_to='./static/files/classSay'),
        ),
    ]
