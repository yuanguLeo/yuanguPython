#!/usr/bin/env python
#_*_coding:utf-8_*_

#方法的重写

class Person:

    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def say_name(self):
        print("我的名字是：{0}".format(self.name))

    def say_age(self):
        print("我的年龄是：{0}".format(self.__age))

class Student(Person):

    def __init__(self,name,age,results):
        Person.__init__(self,name,age)
        self.results = results

    def say_name(self):
        '''重写父类say_name方法'''
        print("报告老师，我的名字是：{0}".format(self.name))


e = Student("张三",18,90)
e.say_name()
e.say_age()

