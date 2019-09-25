#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/25 9:08

'''
python查找“名称”时，local-->Enclosed-->Global-->Built in
local: 指的就是函数或者类的方法内部
Enclosed: 指的是嵌套函数（一个函数包裹另一个函数，闭包）
Global: 指的是模块中的全局变量
Built in: 指的是python为自己保留的特殊名称
'''


#str = "a1b2c3"

def test_01():

    #str = "abcd"

    def test_001():
        #str = "123456"
        print("str: ",str)

    test_001()

test_01()
