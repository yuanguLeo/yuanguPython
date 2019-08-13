#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
测试多分支选择结构
需求：
    输入一个学生的成绩，将其转化成简单描述：
        不及格（小于60）
        及格（60-79）
        良好（80-90）
        优秀（90-100）


score = int(input("请输入成绩："))

if score<60:
    print("您的成绩为：不及格")
elif 60<=score<79:
    print("您的成功为：及格")
elif 80<=score<89:
    print("您的成功为：良好")
elif 90<=score<100:
    print("您的成功为：优秀")
'''
print("***************************")

score = int(input("请输入成绩："))
grade = ''

if (score<60):
    grade = '不及格'
if (60<=score<79):
    grade = '及格'
if (80<=score<89):
    grade = '良好'
if (90<=score<100):
    grade = '优秀'

print("分数为：{0}，成绩为：{1}".format(score,grade))


