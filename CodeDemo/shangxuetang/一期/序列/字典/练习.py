#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/4 9:28

'''
使用字典和列表存储表格


'''

a = [{'name':'高小一','age':18,'salary':30000,'city':'北京'},{'name':'高小二','age':19,'salary':20000,'city':'上海'},{'name':'高小五','age':20,'salary':10000,'city':'深圳'}]
print(len(a))
print(len(a[0]))
# 获得高小二的salary
print(a[1].get("salary"))

# 打印表中的所有的薪资
for i in range(len(a)):
    print(a[i].get("salary"))

# 打印表中所有的数据
for i in range(len(a)):
    print(a[i].get('name'),a[i].get('age'),a[i].get('salary'),a[i].get('city'))



