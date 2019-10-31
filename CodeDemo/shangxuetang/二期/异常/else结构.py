#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/31 9:38

try:
    a = input("请输入第一个数字：")
    b = input("请输入第二个数字：")
    c = float(a) / float(b)

except BaseException as e:
    print(e)

else:
    print(c)
