#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/17 16:10

'''
2-3需求：将用户姓名存到变量中，向用户显示一条消息
'''

a = "Eric"
print("Hello {0},would you like to learn some Python today?".format(a))

'''
2-4需求：将名称分别用小写，大写，首字母大写打印
'''

#小写显示
print(a.lower())

#大写显示
print(a.upper())

#首字母大写
print(a.title())

'''
2-5需求：打印名人名句，包括引号
'''
print('Albrt Einstein said，"A person who never made a mistake never tried anything new"')

'''
2-6需求：将2-5中的名人姓名存在一个变量中，将显示的消息存在另一个变量中，打印
'''
famous_person = 'Einstein'
message = '"A person who never made a mistake never tried anything new"'
print('Albrt '+famous_person+' said, '+message)

'''
2-7需求：剔除名人中的空白
'''
name = ' 元古\t'
print(name)
print(name.lstrip())  #去除后空格
print(name.rstrip())  #去除前空格
print(name.strip())   #去除前后空格


