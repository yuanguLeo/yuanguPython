#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/31 9:48

try:
    a = input("请输入第一个数字：")
    b = input("请输入第二个数字：")
    c = float(a) / float(b)
    print(c)

except ZeroDivisionError:
    print("异常，不能除以0")

except ValueError:
    print("异常，不能讲字符串转成数字")

except BaseException as e:
    print(e)
