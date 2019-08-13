#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
if-elif-else语句
格式：
if 表达式1：
    语句1
elif 表达式2:
    语句2
.....
elif 表达式n：
    语句n
else 表达式4：   #可有可无
    语句e

逻辑：
当程序执行到if-elif-else语句时，首先计算“表达式1”的值，如果“表达式1”的值为真，则执行“语句1”，执行完“语句1”，
则跳过整个if-elif-else语句。如果“表达式1”的值为假，计算“表达式2”的值。如此下去，知道某个表达式的值为真才停止，
如果没有一个真的表达式，且有else.则执行“语句e”

'''

age = int(input())

if age < 0 :
    print("孩子还没有出生！")
elif age < 3:
    print("婴儿")
elif age < 10:
    print("儿童")
elif age < 30:
    print("青年")
elif age < 50:
    print("中年")
elif age < 150:
    print("老年")
else:
    print("老妖怪")

'''
每个el都是对它上面所有表达式的否定
'''
'''
while 表达式：
    语句1
else:
    语句2

逻辑：在条件语句（表达式）为False时执行else中的“语句2”

'''

a = 1

while a <= 3:
    print("leo is a good man")
    a += 1
else:
    print("very very good")