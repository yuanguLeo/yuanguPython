#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 9:02

'''
参数的类型：
1、位置参数
2、默认值参数
3、命名参数
'''


def test_01(a,b,c,d):
    '''测试位置参数，参数个数匹配，参数有序排列'''
    print("{0}-{1}-{2}-{3}".format(a,b,c,d))


def test_02(a,b,c=3,d=4):
    '''测试默认值参数,默认值参数写在最后'''
    print("{0}-{1}-{2}-{3}".format(a,b,c,d))


def test_03(a,b,c,d):
    '''测试命名参数,参数无序,通过形参名称来匹配'''
    print("{0}-{1}-{2}-{3}".format(a,b,c,d))


test_01(1,2,3,4)
test_02(1,2)
test_02(1,2,5)
test_03(c=3,a=1,d=4,b=2)
