#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/10/29 14:35

'''
第四课：改进我们的小游戏
'''


# 测试题：

# 0. 请问以下代码会打印多少次“我爱鱼C！”
# while 'C':
#     print('我爱鱼C!')
#答：无限次


# 1. 请问以下代码会打印多少次“我爱鱼C！”
# i = 10
# while i:
#     print('我爱鱼C!')
#     i = i - 1
#答：打印10次

# 2. 请写出与 10 < cost < 50 等价的表达式
#答：(10< cost) and (cost < 50)

# 3. Python3 中，一行可以书写多个语句吗？
#可以，
# print("my name is yuanguLeo"); print('holle!')

# 4. Python3 中，一个语句可以分成多行书写吗？
#可以
# print("my name is"
#       " yuanguLeo")

# 5. 请问Python的 and 操作符 和C语言的 && 操作符 有何不同？【该题针对有C或C++基础的朋友】


# 6. 听说过“短路逻辑（short-circuit logic）”吗？


# 动动手：

# 0. 完善第二个改进要求（为用户提供三次机会尝试，机会用完或者用户猜中答案均退出循环）并改进视频中小甲鱼的代码。
print('-------------我爱鱼c工作室--------------')
i = 1;
while i <= 3:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    guess = int(temp)
    if guess == 8:
        print("我擦，你是小甲鱼心里的蛔虫吗？")
        print("哼，猜中了也没有奖励！")
        break;
    elif i == 3:
        print('还是猜错了，但是机会用光了，欢迎下次来玩。。。')
        break;
    elif guess < 8 :
        print("猜小了，请继续。。。")
        i += 1;
    elif guess > 8 :
        print("猜大了，请继续。。。")
        i += 1;
print("游戏结束了，不玩了！")

# 1. 尝试写代码实现以下截图功能：
# 输入一个整数：5
# 1
# 2
# 3
# 4
# 5

# temp = int(input("请输入一个整数："))
# i = 1;
# while temp >= 1:
#     print(i)
#     i += 1;
#     temp -= 1;


#2. 尝试写代码实现以下截图功能：
# 输入一个整数：8
#         ********
#        *******
#       ******
#      *****
#     ****
#    ***
#   **
#  *
# sum = int(input("请输入一个整数："))
# while sum >= 1:
#     print(' '*sum + '*'*sum)
#     sum -= 1;




#3. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！