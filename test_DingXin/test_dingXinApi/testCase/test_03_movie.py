#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/1/12 14:55

'''
影片相关
'''
import requests
from test_DingXin.test_dingXinApi.config.config import *

class TestMovie:
    def __init__(self):
        pass

    def test_03_movielist(self):
        '''
        影院放映计划列表(全量)
        /?m=api&a=movielist
        '''
        url = httpIp + '/?m=api&a=movielist'
        movielist = requests.get(url, auth=(name,password))

        print(movielist.url)
        print(movielist.text)
        assert movielist.status_code == 200
        print("===========================================")

    def test_04_movielistincrement(self):
        '''
        该接口按场次更新时间返回 影院放映计划
        /?m=api&a=movielistincrement
        '''

        url = httpIp + '/?m=api&a=movielistincrement'
        tincrement = requests.get(url, auth=(name,password))
        print(tincrement.url)
        print(tincrement.text)
        show_id = tincrement["show_id"]
        print(show_id)
        assert tincrement.status_code == 200
        print("===========================================")

    def test_05_movieshowinfo(self):
        '''
        影院放映计划列表(场次ID)(单个或多个)
        /?m=api&a=movieshowinfo
        '''
        url = httpIp + '/?m=api&a=movieshowinfo'
        data = {
            'show_id'
        }
        movieshowinfo = requests.get(url, auth=(name,password))
        print(movieshowinfo.url)
        print(movieshowinfo.text)
        assert movieshowinfo.status_code == 200
        print("===========================================")

    def test_06_movieinfo(self):
        '''
        影片信息接口(影片编码）
        /?m=api&a=movieinfo
        '''
        url = httpIp + '/?m=api&a=movieinfo'
        data = {
            'movie_id'
        }
        movieinfo = requests.get(url, auth=(name,password))
        print(movieinfo.url)
        print(movieinfo.text)
        assert movieinfo.status_code == 200
        print("===========================================")

if __name__ == '__main__':
    movie = TestMovie()
    movie.test_03_movielist()
    movie.test_04_movielistincrement()
    movie.test_05_movieshowinfo()
    movie.test_06_movieinfo()