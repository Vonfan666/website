#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from websiteBefore.views import websiteBeforeHome

urlpatterns = [
    url(r"home/",websiteBeforeHome.home,name="home"),
    url(r"updateStudentMessage/", websiteBeforeHome.updateStudentMessage, name="updateStudentMessage"),
    url(r"teacherTeam/",websiteBeforeHome.teacherTeam,name="teacherTeam"),
    url(r"studentWork/", websiteBeforeHome.studentWork, name="studentWork"),
    url(r"studentWorkMessage/", websiteBeforeHome.studentWorkMessage, name="studentWorkMessage"),
    url(r"onlineVideo/", websiteBeforeHome.onlineVideo, name="onlineVideo"),
    url(r"aboutSelf/", websiteBeforeHome.aboutSelf, name="aboutSelf"),
]
