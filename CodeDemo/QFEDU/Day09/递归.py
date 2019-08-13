#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
递归调用：一个函数，自己调用自己，称为：递归调用
递归函数：一个调用自己的函数，称为：递归函数

凡是循环能干的事，递归都能干

方式：
1、写出临界条件
2、找这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果

'''

#输入一个大于等于的数，求1+2+3+n的和

def sum(n):
    sum = 0
    for i in range(1,n + 1):
        sum += i
    return  sum

res = sum(5)
print(res)

def sum2(n):
    if n == 1:
        return  1
    else:
        return n + sum2(n-1)

res1 = sum2(5)
print(res1)


















