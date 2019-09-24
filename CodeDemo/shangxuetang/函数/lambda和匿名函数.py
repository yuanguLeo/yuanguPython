#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 9:23

'''


'''

a = lambda a,b,c:a*b*c

b = [lambda a:a*a,lambda b:b*b]

h = [a,a] # 函数也是对象

print(a(2,3,4))
print(b[0](2),b[1](3))
print(h[0](3,3,3))
