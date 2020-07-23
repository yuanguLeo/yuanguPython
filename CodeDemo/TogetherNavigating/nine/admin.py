#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/14 11:15

'''

'''
from user import User

class Admin(User):

    def __init__(self,first_name,last_name,age,city):
        super().__init__(self,first_name,last_name,age,city)
        #self.privileges = '所有权限'

    def show_privileges(self):
        Privileges()

class Privileges():
        privileges = ['can add post','can delete post','can ban user']
        for privilege in privileges:
            print('\n需求9-8：'+privilege)


