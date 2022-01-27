#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/17 16:52

'''
第十四课：字符串：各种奇葩的内置方法
'''

# 测试题：

# 0.还记得如何定义一个跨越多行的字符串吗（请至少写出两种实现的方法）？
#'''  '''

# 1.三引号字符串通常我们用于做什么使用？


# 2.file1 = open('C:\windows\temp\readme.txt', 'r')表示以只读方式打开“C:\windows\temp\readme.txt”这个文本文件，
# 但事实上这个语句会报错，知道为什么吗？你会如何修改？
#file1 = open(r'E:\123.txt', 'r')

# 3.有字符串：str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'，请问如何提取出子字符串：'www.fishc.com'
# str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
# tmpe = str1[16:30]
# print(tmpe)

# 4.如果使用负数作为索引值进行分片操作，按照第三题的要求你能够正确目测出结果吗？
# tmpe = str1[-45:-32]
# print(tmpe)

# 5.还是第三题那个字符串，请问下边语句会显示什么内容？
# str1[20:-36]
#print(str1[20:-36])
#fishc

# 6.据说只有智商高于150的鱼油才能解开这个字符串（还原为有意义的字符串）：
# str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
# print(str1[::3])

# 动动手：

# 0.请写一个密码安全性检查的代码代码：check.py

# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

# 程序演示：
symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

pw = input('请输入密码：')
#判断长度
if len(pw)<=8:
    flag_len = 1
elif 8<len(pw)<16:
    flag_len = 2
else:
    flag_len = 3

flag_con = 0
#判断是否包含特殊字符
for each in pw:
    for each in symbols:
        flag_con += 1
        break

#判断是否是数字
for each in pw:
    for each in nums:
        flag_con += 1
        break

#判断是否是英文
for each in pw:
    for each in chars:
        flag_con += 1
        break

#打印密码级别

if flag_len == 1 or flag_con == 1:
    print('您设置的是低级密码')
elif flag_len == 2 or flag_con == 2:
    print('您设置的是中级密码')
else:
    print('您设置的是高级密码')

# 1.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！

