#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/5 15:46

'''
例题：number_reader.py
'''
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

