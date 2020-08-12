#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/12 11:01

'''

'''

class Employee():
    """雇员"""
    def __init__(self,singer_name,album_name,annual_salarys):
        """构造方法"""
        self.singer_name = singer_name
        self.album_name = album_name
        self.annual_salarys = annual_salarys

    def give_raise(self,annual_salary=3000):
        """annual_salary默认+5000美金"""
        self.annual_salarys += annual_salary
        print(self.singer_name + ' ' + self.album_name + ' , 年薪为： ' + str(self.annual_salarys) )

# employee = Employee('张','三',5000)
# employee.give_raise(5000)