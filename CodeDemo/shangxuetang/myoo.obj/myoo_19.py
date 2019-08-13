#!/usr/bin/env python
#_*_coding:utf-8_*_

#通过继承实现代码复用

class A1:

    def say_a1(self):
        print("A1的对象：",self)

class B1(A1):

    pass

b = B1()
B1.say_a1("张三")

#通过组合实现代码复用

class A2:

    def say_a2(self):
        print("a2,a2,a2")

class B2:

    def __init__(self,a):
        self.a = a

a2 = A2()
b2 = B2(a2)
b2.a.say_a2()