#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/9 9:20
'''
Python支持多重继承，一个子类可以有多个“直接父类”。这样，就具备了“多个父类”的特点，但是由于，这样会被“类的整体层次”搞的异常复杂，尽量避免使用

'''

class A:

    def aa(self):
        print("aa")

class B:

    def bb(self):
        print("bb")

class C(A,B):

    def cc(self):
        print("cc")

c = C()
c.aa()
c.bb()
c.cc()

