#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/4 9:08

aa = {'name': 'yuangu', 'age': 32, 'job': 'test'}

a,b,c = aa  # 获取字典中的键
print(a)
print(b)
print(c)

j,k,l = aa.values()  # 获取值进行操作
print(j)
print(k)
print(l)


e,d,f = aa.items()  # 获取键值对进行操作
print(e)
print(d)
print(f)
print(e[0])
