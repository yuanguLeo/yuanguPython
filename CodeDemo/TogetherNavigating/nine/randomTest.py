#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/14 14:53

'''
需求9-14：
'''

from random import randint

x = randint(1,6)
print(x)

class Die():

    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        self.side = randint(1, self.sides)
        print(self.side)

    def new_roll_die(self,math):
        self.n = 0
        self.math = math
        while self.n < self.math:
            self.roll_die()
            self.n += 1

my_die_01 = Die()
my_die_01.new_roll_die(10)
my_die_02 = Die(10)
my_die_01.new_roll_die(10)
my_die_03 = Die(20)
my_die_03.new_roll_die(20)





