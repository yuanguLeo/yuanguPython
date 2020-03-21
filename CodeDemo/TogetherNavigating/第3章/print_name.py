#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/21 16:26

'''
3-1需求：将姓名存储再一个列表中，以此访问，打印出来
'''
name = ["tom","jack","mary","kobe"]
print("我的名字叫："+name[0].title())
print("我的名字叫："+name[1].title())
print("我的名字叫："+name[2].title())
print("我的名字叫："+name[3].title())

'''
3-2需求：使用3-1的列表，为每人打印一条问候语，抬头为朋友对应名称
'''
print(name[0].title()+", hello")
print(name[1].title()+", hello")
print(name[2].title()+", hello")
print(name[3].title()+", hello")

'''
3-3需求：自己的列表
'''
Commuter = ["car","motorcycle","bus","subway","train"]
print("My "+Commuter[0]+ " is white")

'''

'''