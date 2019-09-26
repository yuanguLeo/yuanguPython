#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/26 22:17

class Person:


    def work(self):
        print("好好工作！")


def paly_game(a):
    print("{0}在玩游戏".format(a))


def work1(a):
    print("好好工作，努力挣钱！")


p = Person()
p.work()

Person.p1 = paly_game
p.p1()

Person.work = work1
p.work()
