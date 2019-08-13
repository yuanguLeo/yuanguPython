#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试多态
'''
注意事项：
1、多态是方法的多态，属性没有多态
2、多态的存在有2个必要条件，继承、方法重写
'''

class Man:

    def eat(self):
        print("饿了，该吃饭了！")

class Chinese(Man):

    def eat(self):
        print("中国人用筷子吃饭")

class English(Man):

    def eat(self):
        print("英国人用叉子吃饭")

def manEat(m):
    if isinstance(m,Man):
        m.eat() #多态。 一个方法调用，根据对象不同调用不同的方法！
    else:
        print("还不能吃饭！")

manEat(Chinese())
