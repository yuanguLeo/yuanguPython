#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/19 9:43

import requests
import unittest

class xiaoTuiCheLogin(unittest.TestCase):

    def setUp(self):

        #信息头
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}

        # 获取工作站接口
        self.workstation = 'http://192.168.55.99/?m=payorder&a=workstation'
        #登录接口
        self.login = 'http://192.168.55.99/?m=payorder&a=login'
        #登录状态查询接口
        self.checkSession = 'http://192.168.55.99/?m=payorder&a=checkSession'
        #订单同步接口
        self.syncOrderData = 'http://192.168.55.99/?m=payorder&a=syncOrderData'
        #注销接口
        self.loginOut = 'http://192.168.55.99/?m=payorder&a=loginOut'


    def workstation_demo(self):
        '''测试获取工作站接口'''
        test_workstation = requests.get(self.workstation)
        workstation_value = test_workstation.json()
        workStationId_value = workstation_value["data"]["info"]
        workStationId_value1 = dict(workStationId_value[0])
        print(workStationId_value1)
        workStationId_value2 = workStationId_value1['workStationId']
        print(workStationId_value2)


    def login_demo(self):
        '''测试登录接口'''
        login_payload = '&data={"userName":"zd03","passWord":"zd03","userLoginAuth":"1","workStationId":"36"}'
        r2 = requests.post(self.login,headers=self.header,data=login_payload)
        print(r2.json())




if __name__ == "__main__":
    unittest.main()

