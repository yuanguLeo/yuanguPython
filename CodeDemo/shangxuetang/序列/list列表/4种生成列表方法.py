#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/22 23:11

# []生成列表
a = [1,2,3,4,"元古"]  # [1, 2, 3, 4, '元古']
print(a)


# list生成列表
b = list("yuanguLeo")  # ['y', 'u', 'a', 'n', 'g', 'u', 'L', 'e', 'o']
print(b)


# range生成列表 range([start,]end[,step])
c = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(c)


# 推导式生成列表
d = list(x*2 for x in range(100) if x%9 == 0)
# [0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198]
print(d)
