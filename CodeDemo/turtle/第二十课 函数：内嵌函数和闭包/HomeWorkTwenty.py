#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/25 17:41

'''
第二十课：函数：内嵌函数和闭包
'''

# 测试题：
# 0.如果希望在函数中修改全局变量的值，应该使用什么关键字？

# 1.在嵌套的函数中，如果希望在内部函数修改外部函数的局部变量，应该使用什么关键字？


# 2. Python 的函数可以嵌套，但要注意访问的作用域问题哦，请问以下代码存在什么问题呢？

# def outside():
#     print('I am outside!')
#
#     def inside():
#         print('I am inside!')
#
# inside()

# 请问为什么代码A没有报错，但代码B却报错了？应该如何修改？
# def outside():
#     var = 5
#
#     def inside():
#         var = 3
#         print(var)
#
#     inside()
#
# outside()

# 代码B：
#
# def outside():
#     var = 5
#
#     def inside():
#         print(var)
#         var = 3
#
#     inside()
# outside()

# 4.请问如何访问funIn()呢？

# def funOut():
#     def funIn():
#         print('宾果！你成功访问到我啦！')
#
#     return funIn()

# 3请问如何访问funIn()呢？

# def funOut():
#     def funIn():
#         print('宾果！你成功访问到我啦！')
#
#     return funIn

# 6.以下是“闭包”的一个例子，请你目测下会打印什么内容？Zm)pT]O


# def funX():
#     x = 5
#
#     def funY():
#         nonlocal x
#         x += 1
#         return x
#
#     return funY
#
#
# a = funX()
# print(a())
# print(a())
# print(a())

# 动动手：
# 0.请用已学过的知识编写程序，统计下边这个长字符串中各个字符出现的次数并找到小甲鱼送给大家的一句话。载后拷贝过去即可）


# 1.请用已学过的知识编写程序，找出小甲鱼藏在下边这个长字符串中的密码，密码的埋藏点符合以下规律
# a) 每位密码为单个小写字母Powered
# b) 每位密码的左右两边均有且只有三个大写字母（由于我们还没有学习到文件读取方法，大家下载后拷贝过去即可）请下载字符串文件：  string2.zip(6.17
# KB, 下载次数: 18404)


# 2.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！



