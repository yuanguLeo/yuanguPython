#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
self代表类的实例，而非类

哪个对象调用方法，那么该方法中的self就代表那个对象

self.__class__  代表类名

'''
class Person(object):

    def run(self):
        print("run")

    def eat(self,food):
        print("eat " + food)

    def say(self):
        print("Hello! my name is %s, I am %d yaers old" %(self.name, self.age))

    def __init__(self,name,age,height,weight):

        #定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

per1 = Person("张三", 20, 180, 60)
per1.say()
















