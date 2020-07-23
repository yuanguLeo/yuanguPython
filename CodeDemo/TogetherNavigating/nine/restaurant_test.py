#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/3 11:33

'''
需求9-10：
'''

from restaurant import Restaurant  #需求9-10
#from restaurantDemo import Admin  #需求9-11
from admin import Admin,Privileges  #需求9-12

my_restaurant = Restaurant('拿渡麻辣香锅','自制冷库')
my_restaurant.increment_number_severd(2)

my_admin = Admin('张','三','30','北京')
my_admin.show_privileges()









