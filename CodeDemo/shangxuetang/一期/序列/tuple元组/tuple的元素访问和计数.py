#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/3 9:09

a = (10,20,50,40,30)
print(a[0])

#a[1] = 50  # 'tuple' object does not support item assignment 元组不允许修改元素
print(a[1])

print(sorted(a))  # [10, 20, 30, 40, 50]  sorted返回的是列表

#zip(列表1，列表2，列表.....)将多个列表对应位置的元素组合
b = (60,70)
c = (80,90)
d = zip(a,b,c)
print(list(d))

