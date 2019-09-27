#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/27 9:22

#测试property版装饰器

class Emp:

    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary


    @property  # 装饰器property关键字
    def salary(self):
        return self.__salary

    @salary.setter  # 针对salary方法写的set方法，用于判断数据的正确性
    def salary(self,salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print("您输入的工资有误，请输入1000--50000之间的正整数！")

e = Emp("元古",18000)
print(e.salary)
e.salary = 20000
print(e.salary)





