#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
from django.db import models


# Create your models here.
class new_message(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)
    title=models.CharField(max_length=1000)
    content=models.CharField(max_length=1000)
    create_time=models.DateTimeField(auto_now_add=True)
    class Meta():
        db_table="new_message"
        verbose_name_plural = "最新消息"

    def __str__(self):
        return self.title


class classsay(models.Model):
    '''课程介绍'''
    id=models.IntegerField(primary_key=True,unique=True)
    classSayName=models.CharField(max_length=20)
    classSayContent=models.CharField(max_length=200)
    classSayImage=models.ImageField(upload_to="./static/files/classSay")
    create_time = models.DateTimeField(auto_now_add=True,blank=True)
    class Meta():
        db_table="classsay"
        verbose_name_plural = "课程介绍"
    def __str__(self):
        return self.classSayName


class trickmessage(models.Model):
    '''招聘信息'''
    id=models.IntegerField(primary_key=True,unique=True)
    companyName=models.CharField(max_length=20)
    trickMoney=models.IntegerField()
    tables_one=models.CharField(max_length=255)
    tables_two = models.CharField(max_length=255)
    tables_three = models.CharField(max_length=255)
    class Meta():
        db_table="trickmessage"
        verbose_name_plural = "招聘信息"
    def __str__(self):
        return self.companyName


class studentmessage(models.Model):

    studentName=models.CharField(max_length=20)
    studentContent=models.CharField(max_length=1000)
    studentImage=models.ImageField(upload_to="./static/files/classSay")
    studentMoney = models.IntegerField()
    studentSex=models.IntegerField(default=1,)
    studentCompany=models.CharField(max_length=255)
    class Meta():
        db_table="studentmessage"
        verbose_name_plural = "学生信息"
    def __str__(self):
        return self.studentName

class  teachermessage(models.Model):

    teacherName=models.CharField(max_length=20,verbose_name="老师名称")
    teacherTitle = models.CharField(max_length=20,verbose_name="老师荣誉")
    teacherLabel=models.CharField(max_length=20,verbose_name="老师标签")
    teacherContent=models.CharField(max_length=400,verbose_name="老师介绍")
    teacherImage=models.ImageField(upload_to="./static/files/classSay",verbose_name="老师图片")
    class Meta():
        db_table="teachermessage"
        verbose_name_plural="老师信息"

    def __str__(self):
        return self.teacherName


#分类
class direction(models.Model):
    '''方向'''
    def __str__(self):
        return self.name
    weight=models.IntegerField(verbose_name="权重(按从大到小排列)",default=0)
    name=models.CharField(verbose_name="名称",max_length=32)
    classifications=models.ManyToManyField("classification")

    class Meta:
        db_table="direction"
        verbose_name_plural="方向（视频方向）"




class  classification(models.Model):
    '''学科'''

    def __str__(self):
        return self.name
    weight=models.IntegerField(verbose_name="权重（按从大到小排列）",default=0)
    name=models.CharField(verbose_name="名称",max_length=32)
    class Meta:
        db_table="classification"
        verbose_name_plural="视频分类"



class level(models.Model):

    title=models.CharField(verbose_name="难度",max_length=32)

    class Meta:
        db_table="level"
        verbose_name_plural="学习难度"

    def __str__(self):
        return self.title


class video(models.Model):
    status_choice=(
        (0,"下线"),
        (1,"上线"),
    )

    level_choice=(
        (0,"初级"),
        (1,"中级"),
        (2,"高级"),
    )
    status=models.IntegerField(verbose_name="状态",choices=status_choice,default=1)
    level=models.ForeignKey(level,on_delete="CASCADE")

    weight=models.IntegerField(verbose_name="权重（按从大到小排列）")
    classification_video=models.ForeignKey("classification",null=True,blank=True,on_delete="CASCADE")

    title=models.CharField(verbose_name="标题",max_length=32)
    summary=models.CharField(verbose_name="简介",max_length=32)
    img=models.ImageField(verbose_name="图片",upload_to="./static/files/Video")
    href=models.CharField(verbose_name="视频地址",max_length=1000)
    create_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="video"
        verbose_name_plural="视频"

    def __str__(self):
        return self.title



