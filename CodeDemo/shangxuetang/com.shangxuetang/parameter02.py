#!/usr/bin/env python
#_*_coding:utf-8_*_

#可变测试

def test01(a,b,*c):
    print(a,b,c)

def test02(a,b,**c):
    print(a,b,c)

def test03(a,b,*c,**d):
    print(a,b,c,d)

test01(10,20,30,40)
test02(10,20,name="张三",age=20)
test03(10,20,30,40,name="张三",age=20)


#强制命名参数：在带星号的“可变参数”后面增加参数，必须在调用的时候“强制命名参数”

def test04(*a,b,c):
    print("强制命名参数：",a,b,c)

test04(10,20,b=30,c=40)

