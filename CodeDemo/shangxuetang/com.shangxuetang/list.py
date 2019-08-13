#!/usr/bin/env python
#_*_coding:utf-8_*_

a = {1,3,'sxt'}
b = {'he','it','sxt'}

#交集
print(a|b)
print(a.union(b))

#并集
print(a&b)
print(a.intersection(b))

#差集
print(a-b)
print(a.difference(b))
