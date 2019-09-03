#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/3 10:02

a = {'name':'yuangu','age':18,'job':'test'}

print(a['name'])
print(a.get("ddd"))  # get获取不到值，不会报错，返回None,可指定返回值：print(a.get("ddd"，'不存在'))
print(a.items())  # 返回所有键值对
print(a.keys())  # 返回所有的健
print(a.values())  # 返回所有的值
print(len(a))  # 返回字典长度
print('name' in a)  # 检测键是否在字典中













