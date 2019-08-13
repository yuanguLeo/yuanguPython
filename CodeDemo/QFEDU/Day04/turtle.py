#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
turtle:是一个简单的绘图工具，绘图窗口的原点(0,0)在正中间，默认海龟的方向右侧

运动命令
forward(d):向前移动d长度
backward(d):向后移动d长度
right(d):向右转动多少度
left(d):向左转动多少度
goto(x,y):移动到坐标为（x,y）的位置
speed(speed):笔画行进的速度，范围0-10


笔画控制命令
up():笔画抬起，在移动的时候不会绘图
down()：笔画落下，移动会绘图
setheading():改变海龟的朝向
pensize():笔画的宽度
pencolor(colorstr):笔画的颜色
reset():恢复所有设置，清空窗口，重置rutrle状态
clear():清空窗口，不好重置turtle
cirele(r,e)：绘制一个圆形，r为半径，e为次数   turtle.circle(50,steps=5)

begin_fill()：开始填充
fillcolor(colorstr)：填充颜色
end_fill()：结束填充
hideturtle():隐藏海龟
showturtle():显示海龟
screensize(x,y)：控制窗口尺寸


其他命令
done():程序继续执行
undo():撤销上一次动作


'''