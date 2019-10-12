#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/12 16:42

'''
单例模式的核心作用是确保一个类只有一个实例，并且提供一个访问实例的全局访问点
'''

class Mysingleton:

    __obj = None
    __init_fiag = True

    def __new__(cls, *args, **kwargs):
        '''将创建的对象放到obj里'''
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self,name):
        '''将init初始化'''
        if Mysingleton.__init_fiag == True:  # 控制初始化次数
            print("init初始化。。。。")
            self.name = name
            Mysingleton.__init_fiag = False

a1 = Mysingleton("a1")
a2 = Mysingleton("a2")
print(a1)
print(a2)
