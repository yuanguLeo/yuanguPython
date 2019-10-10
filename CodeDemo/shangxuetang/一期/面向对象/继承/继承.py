#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/27 9:39

'''
python 支持多重继承，一个子类可以继承多个父类
继承格式：
    class 子类类名(父类1[,父类2,父类3.....])
        类体

'''

class Person:

    def __init__(self,name,age):
        self.name = name
        self.__age = age  # 父类的私有属性，不继承给子类

    def say_age(self):
        print("年龄为：{0}".format(self.__age))

class Student(Person):

    def __init__(self,name,age,score):
        Person.__init__(self,name,age)  # 必须显示的调用父类初始化方法，不然解释器不会调用
        self.score = score

s = Student("元古",18,80)
s.say_age()
#print(s.age)
print(dir(s))
print(Student.mro())  # mro方法，查看继承关系
print(s._Person__age)  # 子类调用父类的私有属性
