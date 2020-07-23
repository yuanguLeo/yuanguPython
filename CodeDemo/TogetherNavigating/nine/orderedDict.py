#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/14 11:23

'''
需求9-11：
'''

from collections import OrderedDict

python_vocabulary = OrderedDict()

python_vocabulary['Global Variable Names'] = '全局变量名'
python_vocabulary['Function Annotation'] = '功能注释'
python_vocabulary['Indentation'] = '缩进'
python_vocabulary['Binary Operator'] = '运算符'
python_vocabulary['String quotes'] = '字符串引号'

for name,language in python_vocabulary.items():
    print(name.title() + " `s favorite language is " + language.title() + ".")


