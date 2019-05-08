#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
from django.contrib import admin

# Register your models here.
from  websiteBefore import models

admin.site.register(models.new_message)
admin.site.register(models.classsay)
admin.site.register(models.trickmessage)
admin.site.register(models.studentmessage)
admin.site.register(models.teachermessage)
admin.site.register(models.direction)
admin.site.register(models.classification)
admin.site.register(models.level)
admin.site.register(models.video)