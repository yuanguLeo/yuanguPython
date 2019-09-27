#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/23 22:29

import copy

'''
测试深拷贝、浅拷贝
'''



def testcopy():
    '''浅拷贝测试'''
    a = [10,20,[1,2]]
    b = copy.copy(a)

    print("a:",a)
    print("b",b)

    b.append(30)
    b[2].append(3)
    print("浅拷贝。。。。")
    print("a：",a)
    print("b: ",b)


def testdeepcopy():

    c = [100,200,[10,20]]
    d = copy.deepcopy(c)

    print("c: ",c)
    print("d: ",d)

    d.append(300)
    d[2].append(30)
    print("深拷贝。。。。。")
    print("c: ",c)
    print("d: ",d)



testdeepcopy()