#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/31 9:48

with open(r"E:\123.txt","r") as f:  # 文件中不能有中文
    content = f.readline()
    print(content)

print("程序结束。。。。")
