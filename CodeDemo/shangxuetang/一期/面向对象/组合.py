#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/12 16:01

'''
is-a关系，我们可以使用“继承”，从而实现子类拥有父类的方法和属性
例如：is-a关系指的是类似的关系：狗是动物，dog is animal. 狗类就应该继承动物类
has-a关系，我们可以使用“组合”，也能实现一个类拥有另一个类拥有另一个类的方法和属性
例如：has-a关系指的是这样的关系：手机拥有CPU,MobilePhone has a CPU
'''

class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen

class CPU:
    def c(self):
        print("麒麟990处理器")
        print("CPU: ",self)

class Screen:
    def s(self):
        print("2k屏")
        print("Screen: ",self)

#方法1：
#c1 = CPU()
#s1 = Screen()
#m = MobilePhone(c1,s1)

#方法2：
m = MobilePhone(CPU(),Screen())
m.cpu.c()
m.screen.s()
