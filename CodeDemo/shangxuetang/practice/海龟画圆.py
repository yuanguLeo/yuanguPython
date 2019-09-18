#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/18 23:05

import turtle

t = turtle.Pen()
t_color = ["red","green","yellow","black","blue"]
t.width(4)
t.speed(0)

for i in range(10):
    t.penup()
    t.goto(0,-i*10)
    t.pendown()
    t.color(t_color[i%len(t_color)])
    t.circle(10+i*10)

turtle.done()