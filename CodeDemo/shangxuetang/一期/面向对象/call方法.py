#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/26 21:58


class Salary():
    '''用于可以通过类名（）的方式调用'''

    def __call__(self,salary):
        print("计算工资啦。。。。")
        yearSalary = salary*12
        daySalary = salary // 22.5
        hourSalary = daySalary // 8

        return dict(yearSalary=yearSalary,monthSalary=salary,daySalary=daySalary,hourSalary=hourSalary)

s = Salary()
print(s(15000))