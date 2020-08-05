#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/5 15:42

'''
例题：number_writer.py
'''
import  json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

