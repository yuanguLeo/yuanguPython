#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/14 10:29

'''

'''
class Restaurant():
    """创建餐馆类"""
    def __init__(self,restaurant_name,cuisine_type):
        """类中的构造方法"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        #设置就餐人数默认值为：0
        self.number_server = 0

    def set_number_severd(self):
        """打印就餐人数"""
        print('目前就餐人数为：' + str(self.number_server))

    def increment_number_severd(self,number):
        """将就餐人数递增"""
        self.number_server += number
        print('目前就餐人数为：' + str(self.number_server))


