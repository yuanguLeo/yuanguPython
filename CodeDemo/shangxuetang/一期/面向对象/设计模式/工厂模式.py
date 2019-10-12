#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/12 16:30

'''
工厂模式实现了创建者和调用者的分离，使用专门的工厂类将选择实现类，创建对象进行统一的管理和控制

'''
class CarFactory:

    def crerteCar(self,brand):
        '''工厂模式'''
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌,无法创建对象"

class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

f = CarFactory()
c1 = f.crerteCar("奔驰")
c2 = f.crerteCar("宝马")
print(c1)
print(c2)
