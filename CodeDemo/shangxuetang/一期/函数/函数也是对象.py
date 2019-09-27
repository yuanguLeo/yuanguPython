#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/20 9:24

# 测试函数也是对象

def test01():
    print("sxtsxt")

test01()
a = test01
a()

print(type(test01))
print(type(a))
print(id(test01))
print(id(a))
