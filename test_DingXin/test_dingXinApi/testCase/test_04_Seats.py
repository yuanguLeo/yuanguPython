#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/1/10 17:27

'''
座位相关接口
'''
import requests
from test_DingXin.test_dingXinApi.config.config import *

class Test_Seats:
    # def __init__(self):
    #     pass

    def test_07_seat(self):
        '''
        座位类型开放渠道
        /?m=api&a=getseatdisplayset
        '''
        url = httpIp + '/?m=api&a=getseatdisplayset'
        seat = requests.get(url, auth=(name,password))
        print(seat.url)
        print(seat.text)
        assert seat.status_code == 200
        print("===========================================")

    def test_08_seatmap(self):
        '''
        根据 影厅ID 获取座位信息
        /?m=api&a=seatmap
        '''
        url = httpIp + '/?m=api&a=seatmap'
        data = {
    #        'hallid' ==
        }
        seatmap = requests.get(url, auth=(name,password))
        print(seatmap.url)
        print(seatmap.text)
        assert seatmap.status_code == 200
        print("===========================================")

# if __name__ == '__main__':
#     seats = Test_Seats()
#     seats.test_07_seat()
#     seats.test_08_seatmap()