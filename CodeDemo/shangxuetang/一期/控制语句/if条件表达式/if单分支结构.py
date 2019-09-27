#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/6 9:27

'''
False,0,0.0,空值列对象（空列表，空集合，空字典，空字符串）,空range对象，空迭代对象

'''

a = input("请输入一个小于10的数字：")
if int(a) < 10:
    print(a)


b = 'False'  # 不是空字符串，所以表达式为True
if b:
    print('打印B')

c = 0  # 0 表示表达式为False，所以不打印
if c:
    print('打印C')


# 控制语句中的表达式不能出现赋值
#if a = 20：
#    print(a)
