#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/15 17:57

'''
需求7-6：三个出口
1、在while循环中使用条件测试结束循环
2、使用变量active来控制循环结束是时机
3、使用break语句在用户输入‘quit’时退出循环
'''
active = True
age = ''
while active:
    age = input('请输入你的年龄：')
    if age != 'quit':
        age = int(age)
        if age < 0:
            print('你输入的年龄不正确 ')
            continue
        if age <= 3:
            print('小于3岁免费观看电影')
            continue
        elif age <= 12:
            print('你的票价为：10美元')
            continue
        else:
            print('你的票价为：15美元')
    else:
        break





