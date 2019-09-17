#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/12 9:15

'''
while 条件表达式：
    循环体语句

需求1：用while循环打印从0-10的数字

'''
num1 = 0
while num1 <= 10:
    print(num1,end=" ")
    num1 += 1
print()
print('***********************')


'''
需求2：利用while循环，计算1-100之间数据的累加和；计算1-100之间偶数的累加和，计算1-100之间奇数的累加和

'''

num2 = 1
sum_all = 0
sum_even = 0
sum_odd = 0
while num2 <= 100:
    sum_all += num2
    if num2 % 2 == 0:
        sum_even += num2
    else:
        sum_odd += num2
    num2 += 1
print('0-100所有数累加和为：',sum_all)
print('0-100所有偶数累加和为：',sum_even)
print('0-100所有奇数累加和为：',sum_odd)


