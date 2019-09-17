#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/17 21:45

'''
break:结束最近的循环
'''
while True:
    a = input("请输入一个字母：")
    if a == "Q" or a == "q":
        print("循环退出")
        break
    else:
        print(a)