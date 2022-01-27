#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/21 18:25

'''
第十九课：我的地盘听我的
'''
# 测试题：

# 0.下边程序会输入什么？

# def next():
#     print('我在next()函数里...')
#     pre()
#
# def pre():
#     print('我在pre()函数里...')
#
# next()

# 我在next()函数里...
# 我在pre()函数里...

# 1.请问以下这个函数有返回值吗？
# def hello():
#     print('Hello FishC!')
# 有，返回None,所有函数都有返回值

# 2.请问Python的return语句可以返回多个不同类型的值吗？
# 可以，默认用逗号隔开，是以元祖的形式返回，你当然也可以用列表包含起来返回

# 3.目测以下程序会打印什么内容：

# def fun(var):
#     var = 1314
#     print(var, end='')
#
# var = 520
# fun(var)
# print(var)

# 1314520

# 4.目测以下程序会打印什么内容？
# var = ' Hi '
# def fun1():
#     global var
#     var = ' Baby '
#     return fun2(var)
#
# def fun2(var):
#     var += 'I love you'
#     fun3(var)
#     return var
#
# def fun3(var):
#     var = ' 小甲鱼 '
#
# print(fun1())

# Baby 小甲鱼 I love you 错误答案
# Baby I love you

# 动动手：

# 0.编写一个函数，判断传入的字符串参数是否为“回文联”（回文联即用回文形式写成的对联，既可顺读，也可倒读。例如：上海自来水来自海上）
# 程序执行结果如图：
# def strs(str):
#     '''判断字符串参数是否为“回文联”'''
#     if str == str[::-1]:
#         print("是回文联！")
#     else:
#         print("不是回文联！")
#
# strs('上海自来水来自海上')
# strs('doajdd')
# str = '上海自来水来自海上'
# print(str[1])
# print(str[-2])


# 1.编写一个函数，分别统计出传入字符串参数（可能不只一个参数）的英文字母、空格、数字和其它字符的个数。
# 程序执行结果如图：
# def strs(var):
#     ''''分别统计传入的字符串的参数个数'''
#     symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
#     chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     nums = '0123456789'
#     x = y = z = l =0
#
#     for i in var:
#         if i in symbols:
#             # 判断特殊字符
#             x += 1
#
#         elif i in chars:
#             # 判断字母
#             y += 1
#
#         elif i in nums:
#             # 判断数字
#             z += 1
#
#         elif i == " ":
#             # 判断空格
#             l += 1
#
#     print('英文字母：{0}个,空格：{1}个，数字：{2}个，特殊字符：{3}个'.format(y,l,z,x))
#
# strs('dd 1w2 @!')


# 2.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！




