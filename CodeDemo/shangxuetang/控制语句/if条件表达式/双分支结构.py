#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/6 9:48

a = input("输入一个数字：")
if int(a) < 10:
    print('输入的数字小于10')
else:
    print('输入的数字大于等于10')

# 三元条件运算符
print('True' if int(a) < 10 else 'False')
