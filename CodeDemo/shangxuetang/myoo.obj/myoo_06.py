#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试私有属性、私有方法

class Employee:

    __company = "高琪老师"

    def __init__(self,name,age):
        self.name = name
        self.__age = age #私有属性

    def __work(self): #私有方法
        print("好好工资，赚钱养家！！！")
        print("年龄：{0}".format(self.__age)) #内部调用私有属性
        print(Employee.__company)  #内部调用全局私有属性


s = Employee("高琪",18)
print(s.name)
print(s._Employee__age) #调用私有属性

s._Employee__work() #调用私有方法
print(Employee._Employee__company) #外部调用全局私有属性

