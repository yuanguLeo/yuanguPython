#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/9 9:39
'''
super()关键字代表父类的定义，不是父类的对象

'''

class A:

    def a(self):
        print("aa",self)

class B(A):

    def b(self):
        super().a()   #A.a(self)
        print("bb",self)

b = B()
b.b()
