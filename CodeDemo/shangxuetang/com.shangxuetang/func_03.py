#!/usr/bin/env python
#_*_coding:utf-8_*_

a = 3;

def test01():
    b = 20
    global a #如果要在函数内改变全局变量的值，增加 global 关键字声明
    print(a)
    a = 300

    print(locals()) #打印输出的局部变量
    print(globals()) #打印输出的全局变量

i = test01()
print(i)
