#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 22:28


'''
嵌套函数（内部函数）：
在函数内部定义的函数

嵌套函数的使用情况：
1、封装-隐藏
    外部无法访问“嵌套循环”
2、嵌套函数，可以让我们在函数内部避免重复代码
3、闭包

'''

def printName(isChinese,name,familyName):
    '''测试嵌套循环'''
    def inner_print(a,b):
        print("{0}{1}".format(a,b))

    if isChinese:
        print(familyName,name)
    else:
        print(name,familyName)

printName(True,"尚","高")
printName(False,"Ivanka","trump")
