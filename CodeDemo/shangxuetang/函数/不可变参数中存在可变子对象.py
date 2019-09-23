#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/23 22:53

'''
测试：传递不可变对象时，不可变对象里包含的子对象是可变的，则方法内修改了这个可变对象，源对象也发生了变化
'''


a = (10,20,[1,2])
print("a: ",id(a))

def test_01(b):
    print("b: ",id(b))
    b[2][0] = 88
    print(b)
    print("b：",id(b))

test_01(a)
print(a)
