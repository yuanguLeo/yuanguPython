#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/10/27 18:26

'''
第五课：闲聊之Python的数据类型
'''

# 测试题：

# 0.在Python中，int表示整型，那你还记得bool、float和str分别表示什么吗？
#int 整型，bool 布尔型，float 浮点型， str 字符串

# 1.你知道为什么布尔类型(bool)的True和False分别用1和0来代替吗？


# 2.使用int()将小数转换为整数，结果是向上取整还是向下取整呢？
#向下取整

# 3.我们人类思维是习惯于“四舍五入”法，你有什么办法使得int()按照“四舍五入”的方式取整吗？


# 4.取得一个变量的类型，视频中介绍可以使用type()和isinstance()，你更倾向于使用哪个？
#type()

# 5.Python3可以给变量命名中文名，知道为什么吗？


# 6. 【该题针对零基础的鱼油】你觉得这个系列教学有难度吗？


# 动动手：

# 0.
# 针对视频中小甲鱼提到的小漏洞，再次改进我们的小游戏：当用户输入错误类型的时候，及时提醒用户重新输入，防止程序崩溃。

# 如果你尝试过以下做法，请举下小手：
# temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# # 这种想法是因为 type(1) 会返回 <class 'int'>，如果 type(temp) 返回结果一致说明输入是整数。
# while type(temp) != type(1):
#     print("抱歉，输入不合法，", end='')
#     temp = input("请输入一个整数：")


# 或者可能这样：
# temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# # not操作符的作用是将布尔类型的结果翻转：即取反的意思，not True == Flase
# while not isinstance(temp, int):
#     print("抱歉，输入不合法，", end='')
#     temp = input("请输入一个整数：")


# 以上方法的思路是正确的，不过似乎忽略了一点儿：就是input()的返回值始终是字符串，所以type(temp)永远是 <class 'str'> ！
# 其实有蛮多的做法可以实现的，不过就目前我们学习过的内容来看，还不足够。
# 所以，在让大家动手完成这道题之前，小甲鱼介绍一点新东西给大家！

# s为字符串
# s.isalnum()所有字符都是数字或者字母，为真返回True，否则返回False。
# s.isalpha()所有字符都是字母，为真返回True，否则返回False。
# s.isdigit()所有字符都是数字，为真返回True，否则返回False。
# s.islower()所有字符都是小写，为真返回True，否则返回False。
# s.isupper()所有字符都是大写，为真返回True，否则返回False。
# s.istitle()所有单词都是首字母大写，为真返回True，否则返回False。
# s.isspace()所有字符都是空白字符，为真返回True，否则返回False。
#
# import  random
# print('-------------我爱鱼c工作室--------------')
# digital = random.randint(1,10)
# i = 1;
# print("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# while i <= 3:
#     #temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
#     #guess = int(temp)
#     temp = input( )
#     if temp.isdigit():
#         guess = int(temp)
#         if guess == digital:
#             print("我擦，你是小甲鱼心里的蛔虫吗？")
#             print("哼，猜中了也没有奖励！")
#             break;
#         else:
#             if i == 3:
#                 print("还是猜错了，机会用光了，欢迎下次来玩。。。")
#                 break;
#             else:
#                 if guess < digital :
#                     print("猜小了。。。")
#                     #i += 1;
#                 else:
#                     print("猜大了。。。")
#                     #i += 1;
#     else:
#         print("抱歉，您的输入有误，请输入一个整数：", end='')
#     i += 1;
# print("游戏结束了，不玩了！")

# import random
#
# times = 3
# secret = random.randint(1, 10)
#
# print('------------------我爱鱼C工作室------------------')
# guess = 0
# print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
#
# while (guess != secret) and (times > 0):
#     temp = input()
#
#     if temp.isdigit():
#         guess = int(temp)
#         if guess == secret:
#             print("我草，你是小甲鱼心里的蛔虫吗？！")
#             print("哼，猜中了也没有奖励！")
#         else:
#             if guess > secret:
#                 print("哥，大了大了~~~")
#             else:
#                 print("嘿，小了，小了~~~")
#             if times > 1:
#                 print("再试一次吧：", end='')
#             else:
#                 print("机会用光咯T_T")
#     else:
#         print("抱歉，您的输入有误，请输入一个整数：", end='')
#
#     times = times - 1  # 用户每输入一次，可用机会就-1
#
# print("游戏结束，不玩啦^_^")


# 例如：
# >> > s = 'I LOVE FISHC'
# >> > s.isupper()
# >> > True
#
# 好了，文字教程就到这里，大家赶紧趁热打铁，改造我们的小游戏吧！


# 1.
# 写一个程序，判断给定年份是否为闰年。（注意：请使用已学过的BIF进行灵活运用）
# 这样定义闰年的: 能被4整除但不能被100整除, 或者能被400整除都是闰年。
# temp = input("请输入一个年份：")
# while not temp.isdigit():
#     temp = input("抱歉，您的输入有误，请输入一个整数：")
# year = int(temp)
# if (year%400) == 0:
#     print(temp + "是闰年。。")
# else:
#     if (year%4) == 0 and (year%100) != 0:
#         print(temp +"是闰年。。。")
#     else:
#         print(temp +"不是闰年")

# 2.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！


