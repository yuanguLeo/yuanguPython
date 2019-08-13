#!/usr/bin/env python
#_*_coding:utf-8_*_

class Phone:

    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen

class CPU:

    def calculate(self):
        print("运算....")
        print("CPU的对象：",self)

class Screen:

    def show(self):
        print("图片显示。。。。")
        print("Screen的对象：",self)

p1 = Phone(CPU(),Screen())
p1.cpu.calculate()
p1.screen.show()