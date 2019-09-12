#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/12 9:34

'''
格式：
for 变量 in 可迭代对象：
    循环体语句

可迭代对象：
1、序列，包含：字符串，列表，元组
2、字典
3、迭代器对象iterator
4、生成器函数generator
5、文件对象
'''

for i in "abcdef":
    print(i,end=" ")
print()


a = {"name":"yuangu","age":18,"job":"软件测试"}
for x in a: # 默认为：键
    print(x)

for x in a.keys():  # 获取键
    print(x)

for x in a.values(): # 获取值
    print(x)

for x in a.items(): # 获取键值对
    print(x)


for x in range(5):
    print(x)


'''
需求：利用while循环，计算1-100之间数据的累加和；计算1-100之间偶数的累加和，计算1-100之间奇数的累加和

'''

num = 0
sum_all = 0
sum_even = 0
sum_odd = 0

for i in range(101): # range(start,end[,step])
    sum_all += i
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
    #num += 1
print('0-100所有数累加和为：',sum_all)
print('0-100所有偶数累加和为：',sum_even)
print('0-100所有奇数累加和为：',sum_odd)
