#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/28 9:03

class Person:

    def __init__(self,name,age):
        self.name = name
        self.__age = age


    def say_age(self):
        print("我的年龄是：{0}".format(self.__age))


    def say_introduce(self):
        print("我的名字是：{0}".format(self.name))


class Student(Person):

    def __init__(self,name,age):
        Person.__init__(self,name,age)

    def say_introduce(self):
        print("报告老师，我的名字是：{0}".format(self.name))

obj = object()
print(dir(obj))

s = Student("元古",18)
s.say_introduce()
print(Student.mro())  # 查看类的层次结构
print(dir(s))
