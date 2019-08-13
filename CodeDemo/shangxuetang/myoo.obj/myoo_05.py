#!/usr/bin/env python
#_*_coding:utf-8_*_

#__call__方法和可调用对象

class SalaryAccount:
    '''工资计算类'''

    def __call__(self,salary):
        print("算工资了。。。")
        yearSalary = salary*12
        daySalary = salary//22.5
        hourSalary = daySalary//8

        return dict(yearSalary=yearSalary,monthSalary=salary,daySalary=daySalary,hourSalary=hourSalary)

s = SalaryAccount()
print(s(10000))