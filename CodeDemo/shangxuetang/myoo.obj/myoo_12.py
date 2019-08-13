#!/usr/bin/env python
#_*_coding:utf-8_*_

#多重继承和mro()

class A:
    def aa(self):
        print("aa")

    def say(self):
        print("AAAA")

class B:
    def bb(self):
        print("bb")

    def say(self):
        print("BBBB")

class C(B,A):  #多重继承的时候，如果继承的父类中有相同的方法名，就看先继承的是谁，先继承的是谁，就优先打印谁的方法
    def cc(self):
        print("cc")

c = C()
print(C.mro()) #打印类的层次
c.say() #解释器寻找方法是“从左到右”的方法寻找，此时会执行B中的say()