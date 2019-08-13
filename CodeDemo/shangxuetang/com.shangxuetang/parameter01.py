#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试参数的类型：位置参数，默认值参数，命名参数

def test01(a,b,c,d):
    print("{0}--{1}--{2}--{3}".format(a,b,c,d))

def test02(a,b,c=30,d=40):
    print("{0}--{1}--{2}--{3}".format(a,b,c,d))

#位置参数
test01(10,20,30,40)
#test01(10,20) #参数不匹配，系统报错：test01() missing 2 required positional arguments: 'c' and 'd'

#默认值参数
test02(10,20)
test02(10,20,300)

#命名参数
test01(a=10,d=40,c=30,b=20)
