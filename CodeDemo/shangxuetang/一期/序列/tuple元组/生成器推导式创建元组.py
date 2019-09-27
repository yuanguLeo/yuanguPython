#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/3 9:20

s = (x*2 for x in range(5))
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())


i = (i*2 for i in range(5))
print(tuple(i))


