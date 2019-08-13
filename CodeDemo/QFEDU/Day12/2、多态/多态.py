#!/usr/bin/env python
#_*_coding:utf-8_*_

from cat import Cat
from mouse import Mouse
from person import Person

'''
多态：一种事物的多种形态

最终目标：人可以喂任何一种动物

'''

tom = Cat("tom")
jerry = Mouse("jetty")

tom.eat()
jerry.eat()

per = Person()
per.foodAnimal(tom)
per.foodAnimal(jerry)




