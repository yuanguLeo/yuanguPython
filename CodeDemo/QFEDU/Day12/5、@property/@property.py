#!/usr/bin/env python
#_*_coding:utf-8_*_

class Person(object):

    def __init__(self,age):
        self.__age = age

    #方法名为受限制的变量去掉双下划线
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age): #去掉下划线.setter
        if age < 0:
            age = 0
        self.__age = age

per = Person(18)
per.age = 100  #相当于调用setAge
print(per.age)  #相当于调用getAge









