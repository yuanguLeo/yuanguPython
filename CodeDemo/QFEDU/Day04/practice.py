#!/usr/bin/env python
#_*_coding:utf-8_*_

#找出列表中的第二大值

listNum = []

num = 0
while num < 10:
    val = int(input())
    listNum.append(val)
    num += 1
print(listNum)

num1 = 0
all = listNum.count(max(listNum))
while num1 < all:
    listNum.remove(max(listNum))
    num1 += 1
print("列表中第二大数为：",max(listNum))