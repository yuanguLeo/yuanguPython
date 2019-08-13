#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试@property装饰器的用法

class Employee:

    @property
    def salary(self):
        print("salary run ....")
        return 10000

e = Employee()
#e.salary()
print(e.salary)
