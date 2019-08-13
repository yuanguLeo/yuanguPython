#!/usr/bin/env python
#_*_coding:utf-8_*_

#需求：从控制台输入一个整数，判断是否是偶数

num1 = int(input("请输入一个数字："))
print(num1)

if num1%2==0:
    print("您输入的是偶数")
else:
    print("您输入的不是偶数")