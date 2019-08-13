#!/usr/bin/env python
#_*_coding:utf-8_*_

s = "print('abcd')"

eval(s)

a = 10
b = 20
c = eval("a+b")
print(c)

dict = dict(a=100, b=200)
d = eval("a+b",dict)
print(d)