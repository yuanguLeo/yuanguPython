#!/usr/bin/env python
# -*- coding: utf-8 -*-
__mtime__ = '2019/8/16'

import turtle

#线的粗细
turtle.width(10)

#第一个圆
turtle.color("blue")
turtle.circle(50)
#第二个圆
turtle.penup()
turtle.color("black")
turtle.goto(120,0)
turtle.pendown()
turtle.circle(50)
#第三个圆
turtle.penup()
turtle.color("red")
turtle.goto(240,0)
turtle.pendown()
turtle.circle(50)
#第四个圆
turtle.penup()
turtle.color("yellow")
turtle.goto(60,-50)
turtle.pendown()
turtle.circle(50)
#第五个圆
turtle.penup()
turtle.color("green")
turtle.goto(180,-50)
turtle.pendown()
turtle.circle(50)




turtle.done()


