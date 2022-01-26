#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/17 16:00

#print("hello_world")

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)