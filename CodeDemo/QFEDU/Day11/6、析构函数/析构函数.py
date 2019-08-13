#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
析构函数：__del__() 释放对象后调用


'''


class Person(object):

    def run(self):
        print("run")

    def eat(self,food):
        print("eat " + food)

    def __init__(self,name,age,height,weight):

        #定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __del__(self):
        print("这里是析构函数！")

per1 = Person("10", 1, 1, 1)
print(per1)

#释放对象
del per1
#print(per1)

def  func():
    per2 = Person("10", 1, 1, 1)

func()






