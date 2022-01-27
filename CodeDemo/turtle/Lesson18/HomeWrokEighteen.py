#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/20 17:15

'''
第十八课：灵活即强大
'''

# 测试题：

# 0.请问以下哪个是形参哪个是实参？
# def MyFun(x):
#     return x ** 3

# y = 3
# print(MyFun(y))

# x是形式参数（形参），y是实际参数（实参）。
# 跟绝大部分编程语言一样，形参指的是函数创建和定义过程中小括号里的参数，而实参指的是函数在调用过程中传递进去的参数。

# 1.函数文档和直接用“  # ”为函数写注释有什么不同？


# 2.使用关键字参数，可以有效避免什么问题的出现呢？
# 关键字参数，是指函数在调用的时候，带上参数的名字去指定具体调用的是哪个参数，从而可以不用按照参数的顺序调用函数

# 3.使用help(print)查看print()这个BIF有哪些默认参数？分别起到什么作用？

# 4.默认参数和关键字参数表面最大的区别是什么？


# 动动手：

# 0.编写一个符合以下要求的函数：
# a) 计算打印所有参数的和乘以基数（base = 3）的结果
# b) 如果参数中最后一个参数为（base = 5），则设定基数为5，基数不参与求和计算。
# def mFun(*param, base=3):
#     result = 0
#     for each in param:
#         result += each
#
#     result *= base
#
#     print('结果是：', result)
#
# mFun(1, 2, 3, 4, 5)


# 1.寻找水仙花数
# 题目要求：如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。例如153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3，
# 因此153是一个水仙花数。编写一个程序，找出所有的水仙花数。
# def daffodils():
#     '''找出所有的水仙花数'''
#     for i in range(100,1000):
#         i = str(i)
#         x1 = int(i[0])*int(i[0])*int(i[0])
#         x2 = int(i[1])*int(i[1])*int(i[1])
#         x3 = int(i[2])*int(i[2])*int(i[2])
#         x4 = x1+x2+x3
#         if int(i) == x4:
#             print("{0}：是水仙花数".format(i))
# daffodils()
#
# def Narcissus():
#     for each in range(100, 1000):
#         temp = each
#         sum = 0
#         while temp:
#             sum = sum + (temp%10) ** 3
#             temp = temp // 10  # 注意这里用地板除
#
#         if sum == each:
#             print(each, end='\t')
#
# print("所有的水仙花数分别是：", end='')
# Narcissus()


# 2.编写一个函数findstr()，该函数统计一个长度为2的子字符串在另一个字符串中出现的次数。例如：假定输入的字符串为“You cannot improve your past, \
# but you can improve your future.Once time is wasted, life is wasted.”，子字符串为“im”，函数执行后打印“子字母串在目标字符串中共出现3次”。
# 程序执行效果：
# def findstr():
#     '''统计字符串出现的次数'''
#     num = 0
#     str = 'You cannot improve your past, but you can improve your future.Once time is wasted, life is wasted.'
#     str1 = 'im'
#     for i in range(len(str)):
#         if str[i] == str1[0]:
#             if str[i+1] == str1[0+1]:
#                 num += 1
#
#     print('im共出现：{0}次！'.format(num))
# findstr()


# 3.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！

