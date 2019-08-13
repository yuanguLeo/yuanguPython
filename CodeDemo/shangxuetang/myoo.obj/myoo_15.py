#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试运算符的重载

class Person:

    def __init__(self,name):
        self.name = name

    def __add__(self, other):

        if isinstance(other,Person):
            return "{0} --- {1}".format(self.name,other.name)

        else:
            print("不是同类对象，不能相加")

    def __mul__(self, other):

        if isinstance(other,int):
            return self.name * other

        else:
            print("不是同类对象，不能相乘")

p1 = Person("张三")
p2 = Person("李四")

x = p1 + p2
print(x)

print(x*3)