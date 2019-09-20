#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/20 8:52

# 测试返回值的基本用法

'''
return 返回值的要点：
    1、如果函数体中包含return语句，则结束函数执行并返回值
    2、如果函数体中不包含return语句，则返回None值
    3、要返回多个返回值，使用列表，元组，字典，集合将多个值“存起来”即可
'''

def test01(a,b):
    return a+b

print(test01(10,20))


def test02():
    print("python")
    return  # 没有指定返回值时，rerurn表示函数结束，并且会返回None
    print("sxt")

print(test02())

def test03(a,b,c):
    return [a*10,b*10,c*10] # 返回多个值，使用列表，元组，字典，集合将多个值“存起来”

print(test03(2,3,4))

