#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试设计模式-单例模式
#重写new方法和构造方法

class singleton:

    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if singleton.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self,name):
        if singleton.__init_flag:  #增加一个判断，使init不被重复调用
            print("init......")
            self.name = name
            singleton.__init_flag = False #被调用一次后，就把__init_flag置为False ，使得不会再次被调用

a = singleton("AA")
b = singleton("BB")

print(a)
print(b)

c = singleton("CC")

print(c)