#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/1/9 15:03

'''
影院信息相关接口
'''

import requests
from test_DingXin.test_dingXinApi.config.config import *

class Test_getcinemainfo:

    def __init__(self):
        pass

    def test_01_CineMainfo(self):
        '''
        影院名称、影院编码
        /?m=api&a=getcinemainfo
        '''
        url = httpIp +'/?m=api&a=getcinemainfo'
        cinemainfo = requests.get(url,auth=(name, password))
        # show_id = cinemainfo().json()["show_id"]
        # print(show_id)
        #打印请求
        print(cinemainfo.url)
        #打印返回值
        print(cinemainfo.text)
        # 断言状态码是否等于200
        assert cinemainfo.status_code == 200
        # hall_id =
        print("===========================================")

if __name__ == '__main__':
    info = Test_getcinemainfo()
    info.test_01_CineMainfo()






