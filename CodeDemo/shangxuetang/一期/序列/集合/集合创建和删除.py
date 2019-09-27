#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/6 8:59

'''
集合是无序可变，元素不能重复，集合的所有元素都是字典中的“键对象”，因此是不能重复且唯一的

'''


# 集合创建
a = {10,20,'sxt'}
b = {5,11,'sxt'}

# 添加
a.add(30)
print(a)


# 删除指定元素
a.remove(10)
print(a)


#交集
print(a | b)
print(a.union(b))


#并集
print(a & b)
print(a.intersection(b))


#差集
print(a-b)
print(a.difference(b))


#清空整个集合
print(a.clear())


