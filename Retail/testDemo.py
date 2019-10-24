#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/23 8:57

import requests
import json
import unittest

class Login(unittest.TestCase):

    def setUp(self):

        #集团登录接口
        self.get_login_01 = "https://passport.yinghezhong.com/validGroupCode"
        self.get_login_02 = "https://passport.yinghezhong.com/login"
        #卖品系统
        self.post_Retil = "https://retail.yinghezhong.com/goodsCategories/list"

        self.headers = {
            "Cookie": "groupCode=27612800",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
            "Referer": "https://passport.yinghezhong.com/login"
        }

        self.request_param_gp = {
            "groupCode": 27612800
        }

        self.request_param = {
            "userLoginName": "yhz",
            "password": "leying",
            "groupCode": 27612800
        }

        self.cookie = ''

    #登录集团版
    def test_login(self):
        request_param_gp = self.request_param_gp
        request_param = self.request_param
        headers = self.headers
        url_01 = self.get_login_01
        s = requests.session()
        login_01 = s.post(url_01, data=request_param_gp, headers=self.headers)
        print("r1cookie:", login_01.cookies)
        print(json.dumps(login_01.text))
        url_02 = self.get_login_02
        login_02 = s.post(url_02, data=request_param, headers=headers, cookies=login_01.cookies)
        print("r2cookie:", login_02.cookies)
        print(json.dumps(login_02.text))
        self.cookie = login_02.cookies

    #选择卖品系统
    def test_retail(self):
        post_retail = self.post_Retil
        response = requests.get(post_retail,cookies=self.cookie)
        print(response.status_code)




if __name__ == "__main__":
    unittest.main()



