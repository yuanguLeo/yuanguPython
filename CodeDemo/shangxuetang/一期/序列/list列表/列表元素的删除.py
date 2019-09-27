#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/23 9:31

# del() 删除列表指定位置元素
a = [10,20,30]
del a[1]
print(a)
print("----------------------")


# pop() 可指定元素，如果没有指定，默认弹出最后一个元素
a.extend([40,50,60])
a.pop()
a.pop(0)
print(a)
print("----------------------")


#remove() 删除首次出现的指定元素，若不在该元素抛出异常
a.extend([10,20,30,40,50,60])
print(a)
a.remove(30) # 指定的是具体元素，不是下标
print(a)
print("----------------------")
