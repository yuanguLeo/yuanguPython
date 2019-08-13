#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试@property装饰器的用法

class Employee:

    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print("您输入的工资有误，请重新输入，工资值在1000--50000之间")

    '''
    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print("您输入的工资有误，请重新输入，工资值在1000--50000之间")
    '''

e = Employee("张三",10000)
#print(e.get_salary())
#e.set_salary(2000)
#print(e.get_salary())

print(e.salary)
e.salary = 20000
print(e.salary)