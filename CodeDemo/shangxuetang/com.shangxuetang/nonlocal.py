#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试nonlocal,global 关键字的用法

a = 10

def outer():
    b = 20

    def inner():
        nonlocal b #声明外部函数的局部变量
        print("innre b:",b)
        b = 30;

        global a
        a = 100
    inner()

outer()
print("a:",a)