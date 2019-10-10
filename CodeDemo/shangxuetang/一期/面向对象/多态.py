#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/10 9:03

'''
多态：是指同一个方法调用由于对象不同可能产生不同的行为

注意：
1、多态是方法的多态，属性没有多态
2、多态的存在有2个必要条件，继承、方法重写

'''

class Man:

    def eat(self):
        print("吃饭")

class ChinseMan(Man):
    def eat(self):
        print("中国人用筷子吃饭")

class EnglishMan(Man):
    def eat(self):
        print("英国人用叉子吃饭")

def manEat(m):
    if isinstance(m,Man):
        m.eat()  # 多态，一个方法调用，根据对象不同调用不同的方法
    else:
        print("不能吃饭啦！")

manEat(ChinseMan())
manEat(EnglishMan())
manEat(Man)
