#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/27 15:28

'''
第二十一课：lambda表达式
'''

# 0. 请使用lambda表达式将下边函数转变为匿名函数？
# def fun_A(x, y=3):
#         return x * y

# 1. 请将下边的匿名函数转变为普通的屌丝函数？
# lambda x : x if x % 2 else None

# 2. 感受一下使用匿名函数后给你的编程生活带来的变化？


# 3. 你可以利用filter()和lambda表达式快速求出100以内所有3的倍数吗？


# 4. 还记得列表推导式吗？完全可以使用列表推导式代替filter()和lambda组合，你可以做到吗？


# 5. 还记得zip吗？使用zip会将两数以元祖的形式绑定在一块，例如：
# list(zip([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
# [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# 但如果我希望打包的形式是灵活多变的列表而不是元祖（希望是[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]这种形式），
# 你能做到吗？（采用map和lambda表达式）


# 6. 请目测以下表达式会打印什么？
# def make_repeat(n):
#         return lambda s : s * n

# double = make_repeat(2)
# print(double(8))
# print(double('FishC'))


