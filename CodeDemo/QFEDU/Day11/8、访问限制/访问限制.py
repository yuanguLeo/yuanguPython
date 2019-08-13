#!/usr/bin/env python
#_*_coding:utf-8_*_

class Person(object):

    def run(self):
        print("run")

    def eat(self,food):
        print("eat " + food)

    def __init__(self,name,age,height,weight,money):

        #定义属性
        self.name = name
        self.__age__ = age
        self._height = height
        self.weight = weight
        self.__money = money  #_Person__money

    def setMoney(self,money):
        self.__money = money

    def getMoney(self):
        return self.__money

per1 = Person("10", 1, 1, 1,10)


#如果要让的内部属性不被外部直接访问，在属性钱加两个下划线(__),
# 在python中如果在属性前加两个下划线，那么这个属性就变成了私有属性

#不能直接访问per1.__money是因为python解释器把__money变成了_Person__money,
#仍然可以用_Person__money去访问，但是强烈建议不要这么干,
# 不同的解释器可能存在解释的变量名不一致

#per1.__money = 0
print(per1.getMoney())

per1._Person__money = 1
print(per1.getMoney())

#在Python中 __xxx__   属于特殊变量，可以直接访问
print(per1.__age__)

#在Python中 _xxx 变量，这样的实例变量外部是可以访问的,
#但是，按照约定的规则，当我们看到这样的变量时，
# 意思是“虽然我可以被访问，但是请把我视为私有变量，不要直接访问我”
print(per1._height)


