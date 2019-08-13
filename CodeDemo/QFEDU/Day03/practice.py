#!/usr/bin/env python
#_*_coding:utf-8_*_

#从控制台输入一个年份，判断是否是闰年
#闰年条件：能被4整除但不能被100整除  或  能被400整除

year = int(input("请输入一个年份："))

if (year % 4 ==0 and year % 100 != 0 ) or year % 400 == 0:
    print("是闰年")

else:
    print("不是闰年")