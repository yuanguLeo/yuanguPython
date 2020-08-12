#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/10 16:10

'''
需求11-1：城市和国家
'''

def get_information(City,Country,population):
    informations = City + ',' + Country + '--' + 'population = ' + population
    return informations

print(get_information('Santiago','Chile','500000'))






