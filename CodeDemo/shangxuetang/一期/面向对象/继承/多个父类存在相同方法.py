#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/9 9:33

class A:

    def aa(self):
        print("aa")

    def say(self):
        print("A.say: AAA")
class B:

    def bb(self):
        print("bb")

    def say(self):
        print("B.say: BBB")

class C(B,A):

    def cc(self):
        print("cc")

c = C()
print(C.mro())  # 打印类的层次结构
c.say()  # 解释器寻找方法是“从左到右”的方式寻找，此时会执行B类中的say()
