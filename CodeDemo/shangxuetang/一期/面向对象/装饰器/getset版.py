#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/27 9:09

'''get、set方法版装饰器'''

class Student:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age


    def get_test_01(self):
        '''get方法'''
        return self.__age


    def set_test_01(self,age):
        '''set方法'''
        if 0<age<120:
            self.__age = age
        else:
            print("您输入的年龄有误!")

s = Student("元古",18)
print(s.get_test_01())
s.set_test_01(1)
print(s.get_test_01())

