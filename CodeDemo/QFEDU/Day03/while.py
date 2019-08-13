#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
while 语句：
    while 表达式：
        语句
逻辑：当程序执行到while语句时，首先计算“表达式”的值，如果“表达式”的值为假，那么结束整个while语句。如果“表达式”为真，
则执行“语句”，执行完“语句”，在去计算“表达式”的值为假，结果整个while语句，如果“表达式”的值还为真，则执行“语句”，
执行完“语句”再去计算“表达式”的值，如此循环往复，直到表达式的值为假才停止

'''

num = 1
while num <= 5 :
    print(num)
    num += 1


#计算1+2+3....+100

sum = 0
num1 = 1
while num1 <= 100:
    sum += num1
    num1 += 1
print("sumb = {0}".format(sum))

#分别打印字符串中的元素

str = "leo is a handsome man"
num2 = 0

while num2 < len(str):
    print("str[num2] =",str[num2])
    num2 += 1