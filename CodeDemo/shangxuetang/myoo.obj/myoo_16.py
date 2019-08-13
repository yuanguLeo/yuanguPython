#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试特殊属性

class A:
    pass

class B:
    pass

class C(A,B):

    def __init__(self,name):
        self.name = name

    def say(self):
        print("cc")

c = C("张三")
c.say()

print(dir(c))
print(c.__dict__)
print(c.__class__)
print(C.__bases__)
print(C.mro())
print(A.__subclasses__())