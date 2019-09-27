#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/28 9:08

import random

a = [20,10,40,30,50,70,60]

a.sort() #默认升序排列
print(a)


a.sort(reverse=True) #默认升序排列
print(a)


random.shuffle(a) #随机排列，打乱顺序
print(a)


#创建新的列表进行排序
print(id(a))
b = sorted(a) #默认升序排列
print(b)
print(id(b))


b = sorted(a,reverse=True) #默认降序排列
print(b)


c = [1,2,3,4,5]
#迭代器 reversed()
d = reversed(c) #反转
print(d) #返回的是迭代器格式，需要自己转成列表
print(list(d))
print(list(d)) #迭代器只能用一次，第二次为空


#返回最大值
print(max(c))


#返回最小值
print(min(c))


#返回总和
print(sum(c))










