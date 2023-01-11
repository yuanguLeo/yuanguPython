#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/1/10 16:05

'''
影厅相关接口
'''

import requests
from test_DingXin.test_dingXinApi.config.config import *

class Test_Hall:
    def test_hall(self):
        '''
        影厅列表
        /?m=api&a=hall
        '''
        url = 'http://' + ip + '/?m=api&a=hall'
        hall = requests.get(url, auth=(name, password))
        print(hall.text)
        assert hall.status_code == 200
        print("===========================================")

    def test_hallincrement(self):
        '''
        影厅列表(更新时间)
        /?m=api&a=hallincrement
        '''
        url = 'http://' + ip + '/?m=api&a=hall'
        data = {
            'update_time' == '2010-01-01'
        }
        hallincrement = requests.get(url, auth=(name, password))
        print(hallincrement.text)
        assert hallincrement.status_code == 200
        print("===========================================")
#
#if __name__ == '__main__':
# test_hall()
# print("=============================================")
# test_hallincrement()

