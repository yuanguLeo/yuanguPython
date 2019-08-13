#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
概念：是一个闭包，把一个函数当做参数，返回一个替代版的函数，本质上就是一个返回函数的函数




'''

#简单装饰器

def funcl():
    print("leo is a good man!")


def funcl1(str):
    print("*************")
    str()

funcl1(funcl)


'''
加强版：
f 是函数funcl的加强版本
'''

def func1():
    print("leo is a good man!")


def func2(str):
    def inner():
        print("*************")
        str()
    return inner

f = func2(func1)
f()


'''
复杂的装饰器


'''

def outer(func):
    def inner1(age):
        if age < 0:
            age = 0
        func(age)
    return inner1


#使用@符号将装饰器应用到函数
@outer  #相当于say  = outer(say)
def say(age):
    print("i am %s yesrs old"%(age))

say(-10)


#通用装饰器

def outer3(func3):
    def inner(*args, **kwargs):
        print("******************")
        func3(*args, **kwargs)
    return inner

@outer3
def say(name,age):
    print("my name is %s, I am %d yesrs old！"%(name,age))

say("张三",20)