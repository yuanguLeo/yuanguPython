#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/25 8:58

'''
nonlocal:用来声明外层的局部变量
global:声明全局变量
'''

a = 100

def test_01():

    b = 10

    def test_001():
        nonlocal b  # 声明外部函数的局部变量
        print("test_001 b: ",b)

        b = 20

        global a  # 声明全局变量
        a = 1000

    test_001()
    print("test_01 b:",b)

test_01()
print("a :",a)


