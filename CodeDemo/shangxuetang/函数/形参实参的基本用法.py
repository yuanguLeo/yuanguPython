#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/19 22:25

def pringMax(a,b): # 形参用于定义的时候

    # 文档字符串（函数的注释）
    '''用于比较两个数的大小，打印较大的值'''

    if a>b:
        print(a,"较大值")
    else:
        print(b,"较大值")

pringMax(10,20) # 实参用于调用的时候
pringMax(100,200)

# 调用help(函数名.__doc__)可以打印输出函数的文档字符串
help(pringMax.__doc__)