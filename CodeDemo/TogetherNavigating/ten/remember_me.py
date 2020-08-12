#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/6 16:43

'''
例题：remember_me.py
'''
#
# import json
#
# def greet_user():
#     """问候用户，并指出其名字"""
#
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#
#     except FileNotFoundError:
#         username = input('请输入姓名: ')
#         with open(filename,'w') as f_obj:
#             json.dump(username,f_obj)
#             print("We'll remember you when you come back, " + username + "!")
#
#     else:
#         print("Welcome back, " + username + "!")
#
# greet_user()




'''
重构remember_me,将函数明确
'''

import  json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input('请输入姓名：')
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()