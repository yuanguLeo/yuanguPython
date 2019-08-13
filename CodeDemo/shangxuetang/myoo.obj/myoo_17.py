#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试对象的浅拷贝和深拷贝

import copy

class Phone:

    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen

class CPU:

    def calculate(self):
        print("计算")
        print("CPU对象：",self)

class Screen:

    def show(self):
        print("显示图片")
        print("screen对象：",self)

c1 = CPU()
s1 = Screen()

p1 = Phone(c1,s1)

#浅拷贝
print("浅拷贝。。。。")
p2 = copy.copy(p1)
print(p1,p1.cpu,p1.screen)
print(p2,p2.cpu,p2.screen)

#深拷贝
print("深拷贝。。。。")
p3 = copy.deepcopy(p1)
print(p1,p1.cpu,p1.screen)
print(p3,p3.cpu,p3.screen)