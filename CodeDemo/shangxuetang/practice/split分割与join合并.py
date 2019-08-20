#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/20 22:47

import time

# split分割
a = "to be or not to be"
print(a.split("be"))


# join合并
b = ["sxt","sxt100","sxt200"]
print("".join(b))


'''
+字符串拼接符与join区别:
+每次创建一个新的对象，效率相对较低
join不管操作多少遍，都是一个对象，效率高
'''

c = ''
time01 = time.time()
for i in range(1000000):
    c += "sxt"
time02 = time.time()
print("运行时间为：" + str(time02-time01))


time03 = time.time()
li = []
for i in range(1000000):
    li.append("sxt")
d = "".join(li)
time04 = time.time()
print("运行时间为：" + str(time04-time03))

