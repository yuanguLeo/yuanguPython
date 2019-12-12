#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/12 17:37

'''
os.walk()方法：
返回一个3个元素的元组（dirpath,dirnames,filenames）
    dirpath：要列出指定目录的路径
    dirnames：目录下的所有文件夹
    filenames：目录下的所有文件

'''

import os

path = os.getcwd()
list_files = os.walk(path)
all_list = []

for dirpath,dirnames,filenames in list_files:
    for dir in dirnames:
        all_list.append(os.path.join(dirpath,dir))
    for files in filenames:
        all_list.append(os.path.join(dirpath,files))

for file in all_list:
    print(file)