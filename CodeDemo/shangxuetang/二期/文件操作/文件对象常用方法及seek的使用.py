#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/12 9:20

with open("a.txt","r") as f:  # ,encoding="utf-8"
    print("文件名称：{0}".format(f.name))
    print(f.tell())
    print("读取文件中的一行内容：{0}".format(str(f.readline())))
    print(f.tell())
    f.seek(6)
    print("读取文件中的一行内容：{0}".format(str(f.readline())))
