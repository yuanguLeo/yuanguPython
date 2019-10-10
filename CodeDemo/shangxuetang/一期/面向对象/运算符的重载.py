#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/10 9:29

class Person:
    def __init__(self,name):
        self.name = name

    def __add__(self, other):
        if isinstance(other,Person):
            return "{0}--{1}".format(self.name,other.name)
        else:
            return "不是相同对象，不能相加"

    def __mul__(self, other):
        if isinstance(other,int):
            return self.name*other
        else:
            return "不是相同对象，不能相加"

p1 = Person("元古")
p2 = Person("盛世")
p = p1 + p2
print(p)
print(p1*3)
