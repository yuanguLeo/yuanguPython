#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019/8/16'

'''
需求：
1、定义多点坐标
2、绘出折现
3、计算起始点和终点的距离
'''

import turtle
import math

#定义多点坐标
x1,y1 = 100,100
x2,y2 = 100,-100
x3,y3 = -100,-100
x4,y4 = -100,100

#绘出折线
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)

#计算起始点和终点的距离
dis = math.sqrt((x1-x4)**2+(y1-y4)**2)
turtle.write(dis)



turtle.done()
