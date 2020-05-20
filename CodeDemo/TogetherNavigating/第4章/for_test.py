#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/20 15:31

'''
需求4-1：将三种披萨名写进列表中，在使用for循环将名称打印出来
'''

pizzas = ["芝士","榴莲","超级至尊"]
for pizza in pizzas:
    print(pizza)
    print(pizza + " :是我最新欢的口味！\n")
print("I really love pizza!")

'''
需求4-2：将三种有共同特征的动物名称写道列表中
'''
animals = ["crocodile","lizard","snake"]
for animal in animals:
    print(animal)
    print("I want to keep a"+ animal+"\n")
print("They are cold-blooded")

'''
需求4-3：使用一个for循环打印数字1-20
'''
for digital_list in range(1,21):
    print(digital_list,end="\t")
print()

'''
需求4-4：打印1-1000000
'''
# for digitals in range(1,1000001):
#     print(digitals)

'''
需求4-5：计算1-1000000的和
'''
list = []
for digitals in range(1,1000001):
    list.append(digitals)
#print(list)
print(min(list))
print(max(list))
print(sum(list))


'''
需求4-6：range()指定第三个数创建一个列表，其中包含1-20个的奇数，使用for循环打印出来
'''
for digitals in range(1,21,2):
    print(digitals,end="\t")
print()

'''
需求4-7：创建一个列表3-30内能被3整除的数字，使用for循环将这个列表打印出来
'''
for digitals in range(3,31,3): #从3开始，步长为：3
    print(digitals,end="\t")
print()

'''
需求4-8：创建1-10的列表，使用for循环打印这些数的立方
'''
lists = []
for list in range(1,11):
    lists.append(list ** 3)
print(lists)

'''
需求4-9：使用列表解析式生成一个列表，其中包含前10个整数的立方
'''
list = [list ** 3 for list in range(1,11)]
print(list,end='\t')

