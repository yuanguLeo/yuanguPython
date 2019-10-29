#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/24 8:45

# 示例：循环输入数字，如果不是数字则处理异常，直到输入88，则结果循环

while True:
    try:
        i = int(input("请输入数字："))
        if i == 88:
            print("退出循环")
            break
    except BaseException as e:
        print(e)





