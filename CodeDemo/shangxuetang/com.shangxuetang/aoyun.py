#!/usr/bin/env python
#_*_coding:utf-8_*_

import turtle
#加粗线
turtle.width(10)

#设置颜色
turtle.color("blue")
#画圆
turtle.circle(50)

#抬笔
turtle.penup()
#移动坐标
turtle.goto(120,0)
#下笔
turtle.pendown()
turtle.color("black")
turtle.circle(50)

#抬笔
turtle.penup()
#移动坐标
turtle.goto(240,0)
#下笔
turtle.pendown()
turtle.color("red")
turtle.circle(50)

#抬笔
turtle.penup()
#移动坐标
turtle.goto(60,-50)
#下笔
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)

#抬笔
turtle.penup()
#移动坐标
turtle.goto(180,-50)
#下笔
turtle.pendown()
turtle.color("green")
turtle.circle(50)

