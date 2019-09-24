#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 22:01


def test_01(a):
    print("test_01:",a)
    if a == 0:
        print("over")
    else:
        test_01(a-1)
    print("test_01***:",a)

test_01(4)


def test_02(b):
    '''递归函数计算阶乘'''
    if b == 1:
        return 1
    else:
        return b*test_02(b-1)

result = test_02(5)
print(result)
