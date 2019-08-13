#!/usr/bin/env python
#_*_coding:utf-8_*_

class Person(object):
    #name = ""
    #age = 0
    #height = 0
    #weight = 0

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

'''
构造函数： __init__()  在使用类创建对象的时候自动调用

注意：如果不显示的写出构造函数，默认会自动添加一个空的构造函数


'''
per1 = Person("张三",18,160,80)
print(per1.name, per1.age)

per2 = Person("李四",20,170,60)
print(per2.name, per2.age)










