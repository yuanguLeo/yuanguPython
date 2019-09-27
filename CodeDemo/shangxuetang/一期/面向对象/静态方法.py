#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/26 9:25

'''
与“类对象”无关的方法，称为“静态方法”
“静态方法”和在模块中定义普通函数没有区别，只不过“静态方法”放到了“类的名字空间里面”，需要通过“类调用”

静态方法格式：
    @staticmethod
    def 静态方法名([形参列表]):
        函数体

重点如下：
1、@staticmathod 必须位于方法上面一行
2、调用静态方法格式：“类名.静态方法名(参数列表)”
3、静态方法中访问实例属性和实例方法会导致错误

'''

class Studen:

    company = "SXT"

    def __init__(self,name,age):
        self.name = name
        self.age = age


    @staticmethod
    def test_01(a,b):
        print("{0}+{1}={2}".format(a,b,a+b))
        #print(self.age)  # 类方法中不能调用实例方法和实例属性

Studen.test_01(1,2)
