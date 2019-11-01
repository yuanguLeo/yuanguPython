#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/1 9:09

'''
自定义异常类一般都是运行时异常，通常继承Exception或其子类即可，命名一般以Error、Exception为后缀

'''

class AgeError(Exception):  # 继承Exception
    def __init__(self,errorInfo):
        Exception.__init__(self)  # 调用父类构造器
        self.errorInfo = errorInfo

    def __str__(self):
        return "年龄错误！"


if __name__ == "__main__":  # 如果为True,则模块是作为独立文件运行，可以执行测试代码
    age = int(input("请输入您的年龄："))
    if age<0 or age>150:
        raise AgeError(age)  # 抛出异常
    else:
        print("您的年龄为：",age)
