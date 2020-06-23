#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/23 10:14

'''
需求9-1：创建Restaurant的类，设置两个属性，restaurant_name和cuisine_type.
创建describe_restaurant()的方法和一个名为open_restaurant()的方法
'''

class Restaurant():
    """创建餐馆类"""
    def __init__(self,restaurant_name,cuisine_type):
        """类中的构造方法"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述方法的作用"""
        print('餐厅名称：' + self.restaurant_name +', 餐厅使用的冰箱类型是：' + self.cuisine_type)

    def open_restaurant(self):
        """打印餐厅正在营业中"""
        print('餐厅：' + self.restaurant_name +'正在营业')

#将类Restaurant的属性赋值给my_restaurant_01
my_restaurant_01 = Restaurant('元古川菜馆','海尔超大冰柜')
#调用类Restaurant下的describe_restaurant()和open_restaurant()方法
my_restaurant_01.describe_restaurant()
my_restaurant_01.open_restaurant()
#调用类Restaurant下的restaurant_name参数
print(my_restaurant_01.restaurant_name)

#二次调用类Restaurant中的describe_restaurant()方法
my_restaurant_02 = Restaurant('拿渡麻辣香锅','自制冷库')
my_restaurant_02.describe_restaurant()

#三次调用类Restaurant中的describe_restaurant()方法
my_restaurant_03 = Restaurant('旧县羊蝎子','没有冰柜')
my_restaurant_03.describe_restaurant()

class User():
    """创建一个用户类"""

    def __init__(self,first_name,last_name,age,city):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def desciribe_user(self):
        """打印用户信息"""
        print(
            '\n姓名：'+self.first_name+self.last_name+
            ', 年龄：'+ self.age +
            ', 所在城市:' + self.city
              )

    def greet_user(self):
        """打印问候语"""
        print('尊敬的：'+self.first_name+self.last_name+'先生/女士：早晨好！')

my_user = User('张','三','30','北京')
my_user.desciribe_user()
my_user.greet_user()


'''
需求9-4：在9-1中添加一个名为：number_served的属性，将其默认值等于0.
'''
