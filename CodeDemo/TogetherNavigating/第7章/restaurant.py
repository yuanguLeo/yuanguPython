#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/12 10:43

'''
需求7-2：餐厅订位
'''
reservations = int(input('请问你几位：'))
if reservations > 8:
    print("目前没有空桌，需求等位，我先帮您取个号，您看可以吗？")
else:
    print('目前不需要等位，您可以直接就餐，请跟我来。。。。')



