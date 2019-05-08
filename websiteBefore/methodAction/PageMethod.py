#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
class Pagination():
    def __init__(self,totalCount,currentPage,perPageNum=6,allPageNum=11):
        self.totalCount=totalCount  #数据总个数 total_count

        try:  #前端传入错误
             self.currentPage=int(currentPage )#当前页是那页
        except Exception as e:
            self.currentPage=1  #可以根据这个值去做判断返回错误信息给前端
        self.currentPageNum=perPageNum  #每页后台返回的数据条数
        self.maxPageNum=allPageNum   #最多显示页面数量


    def start(self): #根据当前页取出 列表的索引起始值
        return (self.currentPage-1)*self.currentPageNum


    def  end(self): #根据当前页取出 列表的索引终止值
        return self.currentPage * self.currentPageNum


    def all_page(self):   #计算并返回 当前数据所需要总页数
        a,b=divmod(self.totalCount,self.currentPageNum)
        if b==0:
            return a
        return a+1


    def foot_all_page(self):   #判断底部返回的页面数值
        if self.all_page() <=self.maxPageNum:  #总页数小于最多显示的页面
            return range(1,self.all_page()+1)  #返回页面显示区间为1到总页面数量
        # 总页数大于最多显示的页面
        part=int(self.maxPageNum/2)

        if self.currentPage<=part+1:  #当前页面小于 显示总页面的一半时
            return range(1,self.maxPageNum+1)  #返回页面区间为 1到显示最大页面

        if self.currentPage+part>self.all_page():  #如果当前页面加上  显示总页面的一半 比总页面大
            return range(self.all_page()-self.maxPageNum+1,self.all_page()+1)  #返回页面区间为 总页面值-页面总数=最后一页的值 到 总页面值


        return range(self.currentPage-part,self.currentPage+part+1)  #当前页面始终在中间