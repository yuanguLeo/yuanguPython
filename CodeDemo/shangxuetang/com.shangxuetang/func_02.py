#!/usr/bin/env python
#_*_coding:utf-8_*_

#函数的返回值
#return 两个作用：1、返回值    2、结束函数的执行

def test(a,b):
    print("计算两个数的和：{0}+{1}".format(a,b))
    return a+b

def test01():
    print("sxt")
    return

def test02(x,y,z):
    return [x*10,y*10,z*10]

c = test(10,20)
print(c)

d = test01()
print(d)

e = test02(2,3,4)
print(e)