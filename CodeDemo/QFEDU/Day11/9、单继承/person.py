#!/usr/bin/env python
#_*_coding:utf-8_*_

class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print("跑")

    def eat(self,food):
        print("eat:" + food)







