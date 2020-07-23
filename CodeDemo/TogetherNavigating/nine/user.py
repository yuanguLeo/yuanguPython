#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/14 11:15

'''

'''

class User():
    """创建一个用户类"""

    def __init__(self,first_name,last_name,age,city,login_attempts):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = login_attempts

    def increment_login_attempts(self,attempts):
        """将login_attempts值+1"""
        self.login_attempts += attempts
        print('\nlogin_attempts值为：'+str(self.login_attempts))

    def reset_login_attemps(self):
        """将login_attempts重置为：0"""
        self.login_attempts = 0
        print("\nlogin_attempts值重置为："+str(self.login_attempts) )


