#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/23 21:52


'''
测试参数的传递
可变对象有：
字典、列表、集合、自定义的对象等
不可变对象有：
int、float、字符串、元组、布尔值 等

'''


#传递可变对象

a = [10,20]

def test_01(m):
    print(id(m))
    m.append(30)

test_01(a)
print(id(a))
print(a)
print("**********************")
#传递不可变对象

b = 100
print(id(b))

def test_02(n):
    print(id(n))
    n += 200
    print(id(n))
    print(n)

test_02(b)
print(b)