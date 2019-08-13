#!/usr/bin/env python
#_*_coding:utf-8_*_



import turtle


t = turtle.Pen()
n = 25
x = -250
y = -250


for i in range(19):

    t.goto(x,y+n*i)
    t.pendown()
    t.forward(18*n)
    t.penup()
