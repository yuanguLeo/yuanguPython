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
print()

'''
需求4-10：使用切片打印列表的前三个元素
'''
print("The first three items in the list are: ")
print(list[:3])

print("The items from the middle of the list are: ")
print(list[3:7])

print("The last from items in the list are:")
print(list[-3:])

'''
需求4-11：创建副本，将其存到变量friend_pizza中
'''
my_pizzas = ["芝士披萨","榴莲披萨","超级至尊披萨"]
friend_pizza = my_pizzas[:]

my_pizzas.append("水果披萨")
print("My favorite pizzas are: ")
for My_pizza_name in my_pizzas:
    print(My_pizza_name)
friend_pizza.append("什锦披萨")
print("My friend`s favorite pizzas are: ")
for friend_pizza_name in friend_pizza:
    print(friend_pizza_name)


'''
需求4-13：使用foods列表，用for循环打印元素名称
'''
my_foods = ['pizza','falafel','carrot','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
print("My faovrite foods are: ")
for my_food in my_foods:
    print(my_food)
print()

friend_foods.append('ice cream')
print("My friend`s favoite foods are: ")
for friend_food in friend_foods:
    print(friend_food)
print()

'''
需求4-13：创建元组，其中又5种元素
'''
ingredients = ('牛肚','羊肉卷','肥牛卷','午餐肉','油麦菜')
for ingredient in ingredients:
    print(ingredient)
print()
#ingredients[0] = '白菜'  #TypeError: 'tuple' object does not support item assignment
#print(ingredients)

ingredients = ('圆生菜','羊肉卷','肥牛卷','午餐肉','大白菜')
for ingredient in ingredients:
    print(ingredient)
print()

