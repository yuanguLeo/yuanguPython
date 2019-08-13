#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
需求：画围棋棋盘
'''
import turtle


t = turtle.Pen()
n = 25
x = -250
y = -250

t.speed(9)
turtle.screensize(400, 400)
t.penup()

for i in range(19):

    t.goto(x,y+n*i)
    t.pendown()
    t.forward(18*n)
    t.penup()

t.left(90)
for i in range(19):

    t.goto(x+n*i,y)
    t.pendown()
    t.forward(18*n)
    t.penup()

t.right(90)

turtle.done()
