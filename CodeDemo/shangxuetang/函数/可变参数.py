#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 9:11

'''
测试可变参数
两种情况：
1、*param(一个星号)，将多个参数收集到一个“元组”对象中
2、**param(两个星号)，将多个参数收集到一个“字典”对象中
注意：
1、在带星号的“可变参数”，后面增加新的参数，必须在调用的时候：“强制命名参数“
'''

#一个星号为元组
def test01(a,b,*c):
    print(a,b,c)


#两个星号为字典
def test02(a,b,**c):
    print(a,b,c)


#*号后还有参数，要强制命名参数
def test03(*c,a,b):
    print(a,b,c)

test01(1,2,3,4)
test02(1,2,name="yuangu",age=18)
test03(3,4,5,a=1,b=2)

