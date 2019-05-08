#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
from  django.shortcuts import redirect,render_to_response,render,HttpResponse


def  home1(req):
    print(req.method)
    if req.method=="GET":
        return HttpResponse("99")
    else:
        return HttpResponse("222")