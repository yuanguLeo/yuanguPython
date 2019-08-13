#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
需求：
    while循环，打印0-10的数字
'''

num = 0
while (num <= 10):
    print(num)
    num += 1

print("*********************")

#计算1-100之间数字的累加和

num1 = 0
sum = 0
while (num1 <= 100):
    sum = sum + num1
    num1 += 1
print(sum)
