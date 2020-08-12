#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/6 17:24

'''
需求10-11：编写一个自己喜欢的数字，使用json.dump()将数字存储到文件中。再编写一个程序，从文件中读取这个值，并打印
"I know your facorite number! It`s___"
'''
# import json
#
# def get_new_diqital():
#     '''将得到的数字存储到文件中'''
#     diqitals = 'diqital_name.json'
#     diqital_name = input('请输入你喜欢的数字：')
#     with open(diqitals,'w') as d_obj_dump:
#         json.dump(diqital_name,d_obj_dump)
#         return diqital_name
#
# def get_diqital():
#     '''获取数字并打印'''
#     diqitals = 'diqital_name.json'
#     with open(diqitals) as d_obj_load:
#         diqital = json.load(d_obj_load)
#     print("I know your facorite number! It`s " + diqital + " !")
#
# get_diqital()

'''
需求10-12：将json.load和json.dump合并到一起
'''

# import json
#
# def get_diqital():
#     '''将json.load和json.dump合并到一起'''
#     diqitals = 'diqitals.json'
#     try:
#         with open(diqitals) as d_obj_load:
#             diqital = json.load(d_obj_load)
#     except:
#         diqital_name = input("请输入自己喜get_new_username():
#     """提示用户输入用户名"""欢的数字：")
#         with open(diqitals,'w') as d_obj_dump:
#             json.dump(diqital_name,d_obj_dump)
#             print("except: I know your facorite number! It`s " + diqital_name + " !")
#     else:
#         print("I know your facorite number! It`s " + diqital + " !")
#
# get_diqital()

'''需求10-13：按需求重构remember_me.py'''

import  json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username =  json.load(f_obj)
    except FileNotFoundError:
        return  None
    else:
        return  username

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

