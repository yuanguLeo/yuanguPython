#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/12 17:31

'''
需求7-4：用户输入披萨配料，没添加一种就打印一条消息，我们将在披萨中添加这种配料，用户输入quit时，循环结束
'''
pizza_a = True
while pizza_a:
    pizza_burden = input("您好，请添加你所需求的配料：")
    if pizza_burden != 'quit':
        print('我们将在披萨中添加: '+pizza_burden+' 这种配料')
    else:
        print('欢迎下次光临。。。')
        pizza_a = False



