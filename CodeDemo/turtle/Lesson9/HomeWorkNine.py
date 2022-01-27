#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/18 16:01

'''
第九课：了不起的分支和循环3
'''

# 测试题：

# 0.下面的循环会打印多少次"I Love FishC"？
# for i in range(0, 10, 2):
#     print('I Love FishC')
#答5次


# 1.下面的循环会打印多少次"I Love FishC"？
# for i in 5:
#     print('I Love FishC')
#答：会报错

# 2.回顾一下break和continue在循环中起到的作用？
#break终止当前循环，跳出循环体，continue是终止本轮循环并开始下一轮循环

# 3.请谈下你对列表的理解？


# 4.请问range(10)生成哪些数？
#0,1,2,3,4,5,6,7,8,9

# 5.目测以下程序会打印什么？
# while True:
#     while True:
#         break
#         print(1)
#     print(2)
#     break
# print(3)
#会打印2,3

# 6.什么情况下我们要使循环永远为真？


# 7. 【学会提高代码的效率】你的觉得以下代码效率方面怎样？有没有办法可以大幅度改进(仍然使用while)？
# i = 0
# string = 'ILoveFishC.com'
# while i < len(string):
#     print(i)
#     i += 1

# 动动手：

# 细节决定成败，看答案前记得自己先敲代码！

# 0.设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。
# 程序演示如图：

# count = 3
# password = "cine123"
# while count :
#     passwd = input("请输入密码：")
#     if passwd == password:
#         print("密码正确，进入程序......")
#         break
#     elif '*' in passwd:
#         print("密码中不能包含'*'号！您还有",count,"次机会！" )
#         continue
#     else:
#         print("密码输入错误！您还有",count-1,"次机会！")
#     count -= 1


# 1.编写一个程序，求100~999之间的所有水仙花数。
# 如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3，因此153就是一个水仙花数。

# for i in range(100,1000):
#     sum = 0
#     temp = i
#     while temp:
#         sum = sum + (temp%10) ** 3
#         temp //= 10
#     if sum == i:
#         print(i)


# 2.三色球问题有红、黄、蓝三种颜色的球，其中红球3个，黄球3个，绿球6个。先将这12个球混合放在一个盒子中，
# 从中任意摸出8个球，编程计算摸出球的各种颜色搭配。
print("red\tyellow\tgreen")
for red in range (0,4):
    for yellow in range (0,4):
        for green in range (2,7):
            if red + green + yellow ==8:
                print(red, '\t', yellow, '\t', green)

# 3.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！

