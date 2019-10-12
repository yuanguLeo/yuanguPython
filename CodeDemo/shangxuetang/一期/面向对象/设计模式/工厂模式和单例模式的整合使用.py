#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/12 17:24

class CarFactory:

    __obj = None
    __init_fiag = True

    def crerteCar(self,brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self):
        if CarFactory.__init_fiag == True:
            print("初始化init....")
            CarFactory.__init_fiag = False

class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

f1 = CarFactory()
a1 = f1.crerteCar("奔驰")
a2 = f1.crerteCar("比亚迪")
print(a1)
print(a2)

f2 = CarFactory()
print(f1)
print(f2)



