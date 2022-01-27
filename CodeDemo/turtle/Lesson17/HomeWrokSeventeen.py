#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/19 17:15

'''
第十七课：函数-python的乐高积木
'''
# 0.你有听说过DRY吗？

# 1.都是重复一段代码，为什么我要使用函数（而不使用简单的拷贝黏贴）呢？
#灵活，方便增删改查

# 2.函数可以有多个参数吗？
# 可以

# 3.创建函数使用什么关键字，要注意什么？

# 4.请问这个函数有多少个参数？
# def MyFun((x, y), (a, b)):
#     return x * y - a * b
#使用“def”关键字，要注意函数名后边要加上小括号“()”，然后小括号后边是冒号“:”，然后缩进部分均属于函数体的内容
# 如果你回答两个，那么恭喜你错啦，答案是0，因为类似于这样的写法是错误的！
# 我们分析下，函数的参数需要的是变量，而这里你试图用“元祖”的形式来传递是不可行的

# 5.请问调用以下这个函数会打印什么内容？
# def hello():
#     print('Hello World!')
#     return
#     print('Welcome To FishC.com!')
# print(hello())
# Hello World!

# 动动手：

# 0.编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。
# def power(x,y):
#     return x ** y
# print(power(2,3))

# def power(x, y):
#     result = 1
#     for i in range(y):
#         result *= x
#     return result
# print(power(2, 3))

# 1.编写一个函数，利用欧几里得算法（脑补链接）求最大公约数，例如gcd(x, y)
# 返回值为参数x和参数y的最大公约数。
# def gcdInt(x,y):
#     list = []
#     f = True
#     while f:
#         if x%y != 0:
#             list.append(x % y)
#             c = x % y
#             x = y
#             y = c
#         else:
#             f = False
#     print('最后的一个非零余数：{0}'.format(min(list)))
# gcdInt(1997,615)
# gcdInt(414,662)


# 2.编写一个将十进制转换为二进制的函数，要求采用“除2取余”（脑补链接）的方式，结果与调用bin()一样返回字符串形式。
def binInt(x):
    list = []
    result = ''
    while x:
        b = list.append(x % 2)
        x = x // 2

    while list:
        result += str(list.pop())
    print('0b'+result)

binInt(100)
print(bin(100))

# 3.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！


