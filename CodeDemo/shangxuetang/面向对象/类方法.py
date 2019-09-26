#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/26 9:13

'''
类方法格式：
    @classmethod
    def 类方法名(cls [,形参列表])：
        函数体

要点如下：
1、@classmethod 必须位于方法上面一行
2、第一个cls必须有，cls指的是“类对象”本身
3、调用类方法格式：“类名.类方法名（参数列表）”。参数列表中，不需要也不能给cls传值
4、类方法中访问实例属性和实例方法会导致错误
5、子类继承父类方法时，传入cls是子类对象，而非父类对象

'''

class Student:

    company = "sxt"  #

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod  # 声明为：类方法
    def test_01(cls):  # 第一个参数必须为cls
        print(Student.company)
        #print(self.name)  # 类方法中不能调用实例方法和实例属性

Student.test_01()  # 使用类名.类方法名调用

