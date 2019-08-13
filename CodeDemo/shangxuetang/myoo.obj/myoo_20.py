#!/usr/bin/env python
#_*_coding:utf-8_*_


#测试设计模式-工厂类
class Car:

    def creare_car(self,brand):
        if brand == "奔驰":
            return Benz()

        elif brand == "宝马":
            return BMW()

        elif brand == "比亚迪":
            return BYD()

        else:
            return "未知品牌，无法识别！！！"

class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

factory = Car()
c1 = factory.creare_car("奔驰")
c2 = factory.creare_car("宝马")
print(c1)
print(c2)