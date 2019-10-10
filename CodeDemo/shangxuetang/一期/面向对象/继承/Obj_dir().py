#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/9 9:11

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_age(self):
        print(self.name,"的年龄是：",self.age)

obj = object()
print(dir())
print("***********************")

p = Person("元古",18)
print(dir(p))
