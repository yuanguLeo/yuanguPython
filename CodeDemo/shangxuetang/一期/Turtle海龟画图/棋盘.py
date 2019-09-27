#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/19 9:11

import turtle

t = turtle.Pen()
''''''
for x in range(1,19):
    t.penup()
    t.goto(-160,180-x*20)
    t.pendown()
    t.goto(180,180-x*20)

for y in range(1,19):
    t.penup()
    t.goto(-180+y*20,160)
    t.pendown()
    t.goto(-180+y*20,-180)






turtle.done()




