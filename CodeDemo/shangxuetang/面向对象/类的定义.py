#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/25 9:47

'''
定义类的语法格式：
class 类名：
    类体

要点：
1、类名必须符合“标识符”的规则，一般规定，首字母大写，多个单词使用“驼峰原则”
2、类体中我们可以定义属性和方法
3、属性用来描述数据，方法（即函数）用来描述这些数据相关的操作

'''


class Student():

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def test_01(self):
        print("{0}的成绩为：{1}分".format(self.name,self.score))

s1 = Student("元古",80)
s1.test_01()
