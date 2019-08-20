#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/20 22:03

'''
格式：[起始偏移量start:终偏移量end:步长step]
特点：包头不包尾
'''

a = 'abcdefghijklmn'
print(a[:])  # abcdefghijklmn


print(a[1:3])  # bc


print(a[3:])  # 表示从下标为3为字符串到最后defghijklmn


print(a[:6])  # 表示从起始量到下标为6-1的字符串abcdef


print(a[::-1])  # 步长为-1，反向提取字符串，相当于倒序nmlkjihgfedcba


# 练习
# 1、将"to be or not to be" 字符串倒序输出
b = "to be or not to be"
print(b[::-1])


# 2、将"sxtsxtsxtsxtsxt" 字符串中所有的s输出
c = "sxtsxtsxtsxtsxt"
print(c[::3])  # print(c[0:100:3])