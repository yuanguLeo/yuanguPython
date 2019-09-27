#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/11 9:03

'''
需求：
    输入一个学生的成绩，将其转化成简单描述：不及格（小于60），及格（60-79），良好（80-90），优秀（90-100）
    可以多分支结构，也可以一个一个判断

'''

# 单分支结构：
score1 = int(input("请输入你的成绩："))
if score1 < 60:
    print("您的成绩为：不及格")
if (60 <= score1 <= 80):
    print("您的成绩为：及格")
if (80 < score1 <= 90):
    print("您的成绩为：良好")
if (90 < score1 <= 100):
    print("您的成绩为：优秀")
else:
    print("您输入的成绩无效")

print('******************************')

# 多分支结构：
score2 = int(input("请输入您的成绩："))
if score2 < 60:
    print("您的成绩为：不及格")
elif (60 <= score1 <= 80):
    print("您的成绩为：及格")
elif (80 < score1 <= 90):
    print("您的成绩为：良好")
elif (90 < score1 <= 100):
    print("您的成绩为：优秀")
else:
    print("您输入的成绩无效")


