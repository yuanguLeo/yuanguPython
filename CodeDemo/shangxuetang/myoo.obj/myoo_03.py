#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试类方法和静态方法
#类方法
class Student:
    company = "影合众"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def say_score(cls):
        print(cls.company)
      #  print(self.name) #类方法和静态方法中，不能调用实例变量，实例方法

Student.say_score()

#静态方法
class Student2:
    @staticmethod
    def add(a,b):
        print("{0}+{1}={2}".format(a,b,(a+b)))
        return a+b

Student2.add(10,20)