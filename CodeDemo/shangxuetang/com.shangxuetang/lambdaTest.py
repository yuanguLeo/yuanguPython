#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试lambda表达式、匿名函数
f = lambda a,b,c,d : a*b*c*d

def test01(a,b,c,d):
    return a*b*c*d

g = [lambda a:a*2,lambda b:b*3,lambda c:c*4]

h = [test01]
print("lambda计算等于：",f(2,3,4,5))
print("lambda列表计算等于：",(g[0](2),g[1](3),g[2](4)))
print("调用函数等于：",test01(2,3,4,5))
print("h等于：",h[0](2,3,4,5)) #函数也是对象
