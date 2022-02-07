#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/14 15:30

'''
第十二课：列表：一个打了激素的数组3
'''

# 测试题：
#
# 0.注意，这道题跟上节课的那道题有点儿不同，回答完请上机实验或参考答案。
# old = [1, 2, 3, 4, 5]
# new = old
# old = [6]
# print(new)
# 如果不上机操作，你觉得会打印什么内容？
#old = [1, 2, 3, 4, 5]

# 1.请问如何将下边这个列表的'小甲鱼'修改为'小鱿鱼'？
# list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 13, 18,8]
# print(list1[1][2])
# list1[1][2] = "['小鱿鱼']"
# print(list1[1][2])

# 2.要对一个列表进行顺序排序，请问使用什么方法？
# list1 = [1, 3, 2, 9, 7, 8]
# list1.sort()
# print(list1)

# # 3.要对一个列表进行逆序排序，请问使用什么方法？
# print(list1.sort())
# list1.reverse()
# print(list1)

# 4.列表还有两个内置方法没给大家介绍，不过聪明的你应该可以自己摸索使用的门道吧：copy()和clear()
# list2= list1.copy()
# print(list2)
# print(list2.clear())

# 5.你有听说过列表推导式或列表解析吗？
# 没听过？！没关系，我们现场来学习一下吧，看表达式：[i * i for i in range(10)]
# 你觉得会打印什么内容？
# [i * i for i in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 居然分别打印了0到9各个数的平方，然后还放在列表里边了有木有？！

# 列表推导式（List comprehensions）也叫列表解析，灵感取自函数式编程语言Haskell。Ta是一个非常有用和灵活的工具，可以用来动态的创建列表，语法如：
# [有关A的表达式 for A in B]

# 例如
# list1 = [x ** 2 for x in range(10)]
# list1
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 相当于
# list1 = []
# for x in range(10):
#     list1.append(x ** 2)

# 问题：请先在IDLE中获得下边列表的结果，并按照上方例子把列表推导式还原出来。
#list1 = [(x, y) for x in range(10) for y in range(10) if x % 2 == 0 if y % 2 != 0]
# list1=[]
# for x in range(10):
#     for y in range(10):
#         if x % 2 == 0:
#             if y % 2 != 0:
#                 list1.append((x, y))
#print(list1)

# 6.活学活用：请使用列表推导式补充被小甲鱼不小心涂掉的部分
# list1 = ['1.用不止步','2.一切皆有可能','3.我能,无限可能!','4.非一般的感觉']
# list2 = ['1.安踏','3.匹克','4.特步','2.李宁']
# list3 = [name +':' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]
# print(list3)
# for slogan in list1:
#     for name in list2:
#         if slogan[0] == name[0]:
#             print(name +':' + slogan[2:])

# 7.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！

