#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/11 9:26

'''
需求：
    输入一个分数，分数在0-100之间，90以上是A，80以上是B，70以上是C，60以上D，60以下是E

'''
'''
score = int(input("请输入您的分数(0-100之间)："))
grade = ''

if score>100 or score<0:
    score = int(input("请输入您的分数(0-100之间)："))
else:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print("分数为：{0}，等级为：{1}".format(score,grade))
'''

score = int(input("请输入您的分数(0-100之间)："))
degree = 'ABCDE'
num = 0

if score>100 or score<0:
    score = int(input("请输入您的分数(0-100之间)："))
else:
    num = score // 10
    if num < 6:
        num = 5
    print(degree[9-num])



