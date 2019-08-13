#!/usr/bin/env python
#_*_coding:utf-8_*_

#作业
#1、从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”
#153=1^3+5^3+3^3
'''
num6 = int(input("请输入一个三位数的数字："))

a = num6 %10   #对10取余数，求个位
b = num6 // 10 %10  #对10取整数之后在对10取余数，求十位
c = num6 // 100 #对100取整数，求百位
if num6 == a**3 + b**3 + c**3:
    print("您输入的是水仙花数")
else:
    print("您输入的不是水仙花数")
'''

#2、从控制台输入一个五位数，如果是回文数就打印“是回文数”,否则打印“不是回文数”
#11111  12321   12221
num7 = int(input("请输入一个五位数字："))
a1 = num7 // 10000
a2 = num7 % 10
a3 = num7 // 10 %10
a4 = num7 //1000 %10

if a1 == a2:
    if a3 == a4:
        print("您输入的是回文数")
    else:
        print("您输入的不是回文数")
else:
    print("您输入的不是回文数")


#3、从控制台输入两个数，输出较大的值
'''
num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))

if num1 > num2:
    print(num1)
else:
    print(num2)
'''
#4、从控制台输入三个数，输入较大的值
'''
num3 = int(input("请输入第一个数字："))
num4 = int(input("请输入第二个数字："))
num5 = int(input("请输入第三个数字："))

if num3 > num4:
    if num3 > num5:
        print(num3)
    else:
        print(num5)
elif num4 > num5:
    print(num4)
else:
    print(num5)
'''
