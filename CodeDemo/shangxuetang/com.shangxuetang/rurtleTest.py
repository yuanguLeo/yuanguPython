#!/usr/bin/env python
#_*_coding:utf-8_*_

import turtle

t = turtle.Pen()
t.width(3)
my_colors = ("red","green","yellow","black")
for i in range(10):
    t.penup()
    t.goto(0,-i*10)
    t.pendown()
    #对颜色个数取余数，为了让颜色有效循环
    t.color(my_colors[i%len(my_colors)])
    t.circle(15+i*10)

turtle.done() #程序执行完，窗口不关闭