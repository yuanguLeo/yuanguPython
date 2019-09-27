#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/26 22:33

'''
私有属性和私有方法要点：
1、通常我们约定，两个下划线开头的属性是私有的(private),其他为公共的(public)
2、类内部可以访问私有属性(方法)
3、类外部不能直接访问私有属性(方法)
4、类外部可以通过"_类名__私有属性(方法)名"访问私有属性(方法)

'''


class Student:

    __workName = "软件测试工程师"  # 类变量

    def __init__(self,name,age):
        '''私有属性'''
        self.name = name
        self.__age = age  # 定义私有属性


    def __test_01(self):  # 定义私有方法
        print("好好上班，努力挣钱！")


s = Student("元古",20)
print(s.name)
print(s._Student__age)  # _类名__私有属性名调用私有属性名
s._Student__test_01()  # _类名__私有属方法调用私有属方法
print(Student._Student__workName)  # 调用类属性

