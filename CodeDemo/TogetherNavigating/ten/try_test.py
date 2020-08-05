#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/30 14:34

'''
异常处理
'''

# try:
#     '''对0整除测试'''
#     print(5/0)
# except ZeroDivisionError:
#     print('ZeroDivisionError：python中不能对0整除')

'''
需求10-6：加法运算
'''
# def num_calculate():
#     try:
#         num_1 = int(input('请输入第一个数字：'))
#         num_2 = int(input('请输入第二个数字：'))
#     except:
#         print('请正确输入数字！')
#     else:
#         count_num = num_1 + num_2
#         print(count_num)
#
# num_calculate()

'''
需求10-7：
# '''
# def num_calculate():
#
#     while True:
#         try:
#             num_1 = int(input('请输入第一个数字：'))
#             num_2 = int(input('请输入第二个数字：'))
#         except:
#             print('请正确输入数字！')
#         else:
#             count_num = num_1 + num_2
#             print(count_num)
#             break
#
# num_calculate()

'''
需求10-8/10-9：读取cats.txt和dogs.txt,将代码放到try-except 代码块中，当文件不存在时，捕获 FileNotFoundError 错误，并打印一条友好消息
'''

# def file(file_names):
#     for file_name in file_names:
#         try:
#             with open(file_name) as pet:
#                 mag = pet.read()
#
#         except FileNotFoundError:
#             #print('请确认该目录下是否存在此文件:' + file_name)
#             pass
#
#         else:
#             print(mag)
#
# file_name = ['cats.txt','dogs.txt','pigs.txt']
# file(file_name)

'''
需求10-10：
'''
def counts():
    try:
        with open('count.txt') as count_num:
            count = count_num.read()
    except FileNotFoundError:
        print("没有可显示的文件")
    else:
        print(count.lower().count('the'))

counts()





