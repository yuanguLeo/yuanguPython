#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/23 10:32


'''需求10-1练习第一步'''
#learning_pythons = 'E:\YuanGuPython\CodeDemo\TogetherNavigating\ten\learning_python.txt'
with open('learning_python.txt',encoding='utf-8') as file_01:
    learning_python = file_01.read()
    print('练习1:'+learning_python.rstrip())
    print()

'''需求10-1练习第二步'''
files_02 = 'learning_python.txt'
with open(files_02,encoding='utf-8') as file_02:
    for file in file_02:
        print('练习2:'+file.rstrip())

'''需求10-1练习第三步'''
list_files = ''
files_03 = 'learning_python.txt'
with open(files_03,encoding='utf-8') as file_03:
    list_file =  file_03.readlines()

for file in list_file:
    list_files += file.rstrip()

print(list_files)
print(len(list_files))
print()

'''需求10-2:将文件中的python替换为C'''
with open(files_03,encoding='utf-8') as file_04:
    for file in file_04:
        message = file.replace('Python','C')
        print(message)

'''需求10-3：将访客输入的姓名写入到guest.txt中'''

# with open('guest.txt','a') as guest_lists:
#     name = input("请输入你的名字：")
#     guest_lists.write(name + '\n')

'''需求10-4：编写while循环，提示用户输入名字，输入后打印一条问候语，将访客记录添加到guest_book.txt中，每条记录独占一行'''

# with open('guest_book.txt','a') as guest_books:
#     while True:
#         guest_name = input('请输入你的名字：')
#         if guest_name != 'q':
#             print('欢迎光临：' + guest_name + ' 先生/女士')
#             guest_books.write(guest_name + ' 先生/女士光临大驾！\n')
#         else:
#             break

'''需求10-5：编写一个while 循环，询问用户为何喜欢编程。每当用户输
入一个原因后，都将其添加到一个存储所有原因的文件中'''

# with open('why_guest.txt','a') as why_guests:
#     while True:
#         why_guest =input ('请输入你喜欢编程的原因：')
#         if why_guest != 'q':
#             why_guests.write('我喜欢编程的原因是：'+ why_guest + '\n')
#         else:
#             break