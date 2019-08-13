#!/usr/bin/env python
#_*_coding:utf-8_*_


class Person(object):
    name = ""
    age = 0
    height = 0
    weight = 0

    def run(self):
        print("run")

    def eat(self,food):
        print("eat " + food)

    def openDoor(self):
        print("我已经打开了冰箱门")

    def fillEle(self):
        print("我已经把大象装进冰箱了")

    def closeDoor(self):
        print("我已经关闭了冰箱门")

per = Person()


'''
访问对象的属性
格式： 对象名.属性名 = 新值

'''

per.name = "tom"
per.age = 12
per.height = 160
per.weight = 80

print(per.name, per.age, per.height, per.weight)

'''
访问对象的方法
格式：对象名.方法名(参数列表)

'''

per.openDoor()
per.fillEle()
per.closeDoor()
per.eat("apple") #传参数的











