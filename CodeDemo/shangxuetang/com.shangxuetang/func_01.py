#!/usr/bin/env python
#_*_coding:utf-8_*_


def func_01(a,b):
    '''对比两数字，打印较大值'''
    if a>b:
        print(a,"较大值")

    else:
        print(b,"较大值")

func_01(10,20)
func_01(30,20)
help(func_01.__doc__)