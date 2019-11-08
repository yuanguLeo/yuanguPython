#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/7 9:11

a = ["尚学堂\n","百战程序员\n","yuangu\n"]
b = [line.rstrip()+" #"+str(index) for index,line in enumerate(a)]
print(b)

c = []
for index,line in enumerate(a):
    c.append(line.rstrip()+" #"+str(index))
print(c)


