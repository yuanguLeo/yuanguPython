#!/usr/bin/env python
#_*_coding:utf-8_*_


#重写object的__str__()


class Person: #默认继承object类

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "名字是：{0}".format(self.name)

p = Person("张三")
print(p)
