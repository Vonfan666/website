#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
# Generated by Django 2.1.5 on 2019-04-06 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websiteBefore', '0012_auto_20190406_1205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classsay',
            options={'verbose_name_plural': '课程介绍'},
        ),
        migrations.AlterModelOptions(
            name='new_message',
            options={'verbose_name_plural': '最新消息'},
        ),
        migrations.AlterModelOptions(
            name='studentmessage',
            options={'verbose_name_plural': '学生信息'},
        ),
        migrations.AlterModelOptions(
            name='trickmessage',
            options={'verbose_name_plural': '老师信息'},
        ),
        migrations.AlterModelTable(
            name='classsay',
            table='ClassSay',
        ),
        migrations.AlterModelTable(
            name='new_message',
            table='new_message',
        ),
        migrations.AlterModelTable(
            name='studentmessage',
            table='studentMessage',
        ),
        migrations.AlterModelTable(
            name='trickmessage',
            table='学院就业',
        ),
    ]
