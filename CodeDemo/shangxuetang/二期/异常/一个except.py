#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/31 9:48

# 示例：循环输入数字，如果不是数字则处理异常，直到输入88，则结束循环

while True:

    try:
        a = int(input("请输入一个数字："))
        if a == 88:
            print(a)
            break

    except BaseException as e:
        print(e)


