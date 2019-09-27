#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/23 8:57

# append() 效率快，推荐使用
a = [10,20]
a.append(30)
print(a)
print("-----------------------")


# +运算符操作
print(id(a))
a = a + [40]
print(a)
print(id(a))
print("-----------------------")


# extend() 用于两个列表的整合，效率高
print(id(a))
a.extend([50,60])
print(a)
print(id(a))
print("-----------------------")


# insert将指定元素插入到列表对象中的任意指定位置
a.insert(3,100)
print(a)
print("-----------------------")


# 乘法扩展
a = a * 3
print(a)
print("-----------------------")

