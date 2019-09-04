#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/4 8:50


#添加
a = {'name':'yuangu','age':32,'job':'test'}
a['sex'] = '男'  # 添加的值，在字典中不存在，则添加，如存在，则修改
a['sex'] = '女'
print(a)

#update
b = {'sex':'男','add':'北京','money':'2000'}
a.update(b)  # update的值，在字典中不存在，则添加，如存在，则修改
print(a)


#删除
del (a['sex'])  # 删除键值对
print(a)

c = a.pop('name')  # 将键删除，值赋给c
print(c)

a.clear() # 删除整个字典
print(a)

a = {'name': 'yuangu', 'age': 32, 'job': 'test', 'sex': '男', 'add': '北京', 'money': '2000'}
a.popitem()  # 随机删除和返回该键值对
print(a)
