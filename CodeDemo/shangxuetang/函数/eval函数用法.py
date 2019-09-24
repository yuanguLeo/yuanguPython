#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 9:42

'''
功能：将字符串str当成有效的表达式来求值并返回计算结果

'''
s = "print('abcd')"
eval(s)


a = 10
b = 20
c = eval('a+b')
print(c)


dict1 = dict(a=100,b=200)
d = eval("a+b",dict1)
print(d)
