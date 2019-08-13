#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试super()，代表父类的定义，而不是父类的对象

class A:

    def say(self):
        print("A:",self)

class B(A):

    def say(self):
        A.say(self)
        super().say()
        print("B:",self)

b = B()
b.say()