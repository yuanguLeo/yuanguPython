#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
重写：将函数重写定义写一遍

__str__()：在调用print打印对象时自动调用，是给用户用的，是一个描述的对象的方法
__repr__():是给机器用的，在python解释器里面直接敲对象名，在回车后调用方法

注意：在没有str时，且有repr,str = repr

优点：当一个对象的属性值很多，并且都需要打印，重写了__str__方法后，简化了代码
'''

class Person(object):

    def __init__(self,name,age,height,weight):

        #定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return "%s-%d-%d-%d" % (self.name, self.age, self.height, self.weight)

per1 = Person("10", 1, 1, 1)
print(per1)












