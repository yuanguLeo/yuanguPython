#!/usr/bin/env python
#_*_coding:utf-8_*_

#将工厂模式与单例模式整合

class Car:

    __obj = None
    __init_flag = True

    def creare_car(self,brand):
        if brand == "奔驰":
            return Benz()

        elif brand == "宝马":
            return BMW()

        elif brand == "比亚迪":
            return BYD()
        else:
            print("品牌不对，无法识别！！！")

    def __new__(cls, *args, **kwargs):
        if Car.__obj == None:
            Car.__obj = object.__new__(cls)

        return Car.__obj

    def __init__(self):
        if Car.__init_flag:
            print("Car init.......")
            Car.__init_flag = False


class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

factory = Car()
c1 = factory.creare_car("奔驰")

factory1 = Car()
c2 = factory1.creare_car("宝马")

print(c1)
print(c2)

print(factory)
print(factory1)