#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/3 9:34

'''
字典是“键值对”的无序可变序列
键：是任意的不可变数据，比如：整数，浮点数，字符串，元组。但是：列表，字典，集合这些可变的对象，不能作为“键”，键不可重复
值：可以是任意的数据，并且可重复

'''

#1、{}创建

a = {"name":"yuangu","age":18,"job":"test"}
print(a)


#2、dict创建
b = dict(name = "yuangu",age = 18 ,job ="test")
print(b)
c = dict([("name","yuangu"),("age",18)])
print(c)


#3、zip()创建字典
k = ["name","job","age"]
v = ["yuangu","test",18]
j = zip(k,v)
print(dict(j))


#4、fromkeys创建值为空的字典
d = dict.fromkeys(["name","job","age"])
print(d)
