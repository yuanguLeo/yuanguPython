#!/usr/bin/env python
#_*_coding:utf-8_*_

#打印出所有三位数中的水仙花数
'''
num = 100

while  num <= 999:
    a = num % 10
    b = num // 10 % 10
    c = num // 100
    if num == a**3 + b**3 + c**3:
        print(num)
    num += 1
'''

#告诉我五位数中有多少个回文数
'''
sum = 0
num1 = 10000


while num1 <= 99999:

    a1 = num1 // 10000
    a2 = num1 % 10
    a3 = num1 // 10 %10
    a4 = num1 //1000 %10

    if a1 == a2:
        if a3 == a4:
            sum+=1
    num1 +=1

print("五位数中有回文数的个数为：%d"%sum)
'''

#从控制台输入一个数，判断是否是质数
'''
num2 = int(input("请输入一个数字："))

if num2 == 2:
    print("是质数")

index = 2
while index < num2:
    if num2 % index == 0:
        print("不是质数")
        break
    num2 += 1


if index == num2:
    print("是质数")
'''

#从控制台输入一个数，分解质因数
#90=2*3*3*5
'''
num = int(input())
i = 2  #从最小的质数开始

while num != 1:
    if num % i == 0:  #对质数取余数
        print(i)
        num //= i  #对质数取整
    else:
        i += 1  #不满足条件，质数+1
'''

#从控制台输入一个字符串，返回这个字符串中有多少个单词

str = input("请输入一句话:")
str1 = str.strip()
index = 0
count = 0

while index < len(str1):
    while str1[index] != " ":
        index += 1
        if index == len(str1):
            break

    count += 1

    if index == len(str1):
        break

    while str1[index] == " ":
        index += 1

print(count)




#从控制台输入一个字符串，打印出这个字符串中所有数字字符的和
'''
str1 = input("请输入一个字符串：")
index1 = 0
sum1 = 0

while index1 < len(str1):
    if str1[index1] >= "0" and str1[index1] <= "9":
        sum1 += int(str1[index1])
    index1 += 1

print("sum1 = %d"%sum1)
'''
'''
字符串比较大小：
从第一个字符开始比较，谁的ASCII值大谁就大，如果相等会比较下一个字符的ASCII值大小，那么谁的值大谁就大
'''