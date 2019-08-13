#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试继承的基本使用

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_age(self):
        print("姓名，年龄，成绩不知道")

class Student(Person):

    def __init__(self,name,age,results):
        Person.__init__(self,name,age) #必须显示调用父类初始化方法，不然解释器不会去调用
        self.results = results

#Student——>Person——>object类
print(Student.mro())
s = Student("张三",18,80)
s.say_age()
print(s.name)