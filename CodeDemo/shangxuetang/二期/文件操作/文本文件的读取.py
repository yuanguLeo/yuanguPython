#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/6 9:28

# 读取一个文件的前4个字符

with open(r"a.txt","r",encoding="utf-8") as a:
    print(a.read(4),end="")
    print("*********************")

# 文件较小，一次将文件内容读入到程序中

with open(r"a.txt","r",encoding="utf-8") as b:
    print(b.read())
    print("*********************")

# 按行读取一个文件

with open(r"a.txt","r",encoding="utf-8") as c:
    while True:
        f = c.readline()
        if not f:
            break
        else:
            print(f,end="")
print()
print("*********************")

# 使用迭代器读取文本文件
with open(r"a.txt","r",encoding="utf-8") as d:
    for i in d:
        print(i,end="")
print()
print("*********************")
