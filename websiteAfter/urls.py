#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
from django.contrib import admin
from django.urls import path
from websiteAfter.views import websiteAfterHome

urlpatterns = [
    path("home1/",websiteAfterHome.home1,name="home1")
]