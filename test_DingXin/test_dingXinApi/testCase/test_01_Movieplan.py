#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/1/9 15:03

'''
影院信息相关接口
'''

import requests
from test_DingXin.test_dingXinApi.config.config import *

class Test_getcinemainfo:
    def test_CineMainfo(self):
        '''
        影院名称、影院编码
        /?m=api&a=getcinemainfo
        '''
        url = 'http://'+ ip +'/?m=api&a=getcinemainfo'
        cinemainfo = requests.get(url,auth=(name, password))
        print(cinemainfo.text)
        assert cinemainfo.status_code == 200 #断言状态码是否等于200
        print("===========================================")
#
#test_CineMainfo()
#
# if __name__ == '__main__':
#     self.test_CineMainfo()






