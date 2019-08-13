#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
需求：
    输入一个分数，分数在0-100之间，90以上是A，80以上是B，70以上是C，60以上是D，60以下是E


score = int(input("请输入一个数字:"))
grade = ''

for i in range(3):
    if (score>100 or score<0):
        #print("请输入0-100的数字")
        score1 = int(input("请输入0-100的数字："))
    else:
        if (90<score<=100):
            grade = "A"
        elif (score>=90):
            grade = 'b'
        elif (score >=70):
            grade = 'c'
        elif (score >=60):
            grade = 'd'
        elif (score <60):
            grade = 'e'
print("成绩是：{0}，等级为：{1}".format(score,grade))

'''
print("************************************")

score = int(input("请输入一个数字:"))
degree = 'ABCDE'

num = 0

if(score>100 or score<0):
    score = int(input("请输入0-100的数字："))
else:
    num = score//10
    if num <6:
        num = 5
print("分数是{0}，等级是{1}".format(score,degree[9-num]))


