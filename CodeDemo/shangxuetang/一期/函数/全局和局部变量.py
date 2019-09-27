#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/20 9:41

# 测试全局和局部变量

a = 3  # 全局变量

def test01():

    b = 4  # 局部变量
    print(b*10)
    #print(a)

    global a  # 如果要在函数内改变全局变量的值，增加global关键声明
    a = 300
    print(a)

    print(locals())  # 打印输出的局部变量
    print(globals())  # 打印输出的全局变量

test01()
print(a)
