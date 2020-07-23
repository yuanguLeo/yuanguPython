#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/15 17:39

'''
需求7-5：电影票，三岁以下免费，3-12岁为10美元，超过12岁为15美元，编写一个循环，询问用户年龄
'''
while True:
    age = int(input('请输入你的年龄：'))
    if age <= 3:
        print('小于3岁免费观看电影')
        continue
    elif age <= 12:
        print('你的票价为：10美元')
        continue
    else:
        print('你的票价为：15美元')
        break


