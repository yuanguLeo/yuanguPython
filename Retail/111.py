#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/22 21:34


#获取APP版本号接口
import unittest
import requests


class xiaoTuiCheLogin(unittest.TestCase):
    def setUp(self):
        self.post_url = 'http://192.168.55.99/?m=payorder&a=login'
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}

    def test_new_login(self):
        """正常传参，"""
        #payload = '&data={"userName":"testone","passWord":"1111","userLoginAuth":"1","workStationId":"68"}'
        payload = '&data={"userName":"zd03","passWord":"zd03","userLoginAuth":"1","workStationId":"36"}'
        rep = requests.post(self.post_url,headers=self.header,data=payload)
        print("rep结果：",rep)
        result = rep.json()
        print("打印结果:", result)
        # self.assertEqual(rep.status_code, 200, msg='返回status不是200')
        self.assertEqual(result['code'], 1, msg='请求失败')


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
