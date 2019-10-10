#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/9 9:15

#str 帮助打印返回的信息

class Person:

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "名字为：{0}".format(self.name)

p = Person("元古")
print(p)  # 未重写之前打印结果为：<__main__.Person object at 0x000000000212D4E0>

