#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/1/10 16:05

'''
影厅相关接口
'''

import requests
from test_DingXin.test_dingXinApi.config.config import *



class Test_Hall:
    hall_id = []

    # def __init__(self):
    #     pass

    def test_02_hall(self):
        '''
        影厅列表
        /?m=api&a=hall
        '''
        url = http_ip + '/?m=api&a=hall'
        hall = requests.get(url, auth=(name, password))
        print(hall.url)
        print(hall.text)
        assert hall.status_code == 200
        print("===========================================")

    def test_03_hallincrement(self):
        '''
        影厅列表(更新时间)hallincrement
        /?m=api&a=hallincrement
        '''
        url = http_ip + '/?m=api&a=hall'
        data = {
            'update_time' == '2010-01-01'
        }
        hallincrement = requests.get(url, auth=(name, password))
        print(hallincrement.url)
        print(hallincrement.text)
        assert hallincrement.status_code == 200
        print("===========================================")

# if __name__ == '__main__':
#     hall = Test_Hall()
#     hall.test_02_hall()
#     hall.test_03_hallincrement()

