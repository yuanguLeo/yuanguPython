#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/1/5 15:49

'''
单机324专资版本接口测试
订单查询接口 orderQuery
'''
import unittest
import requests
import json

class test_orderQuery(unittest.TestCase):
    def test_orderQuery(self):

        url_orderQuery = "http://172.16.3.111/"
        date = {
            "cinemaCode":"13065601",
            "redeemCode":"298810443108",
                }
        response = requests.get(url_orderQuery, params=date)
        print(response.text)
        assert response.status_code == 200

#print(test_orderQuery('13065601','298810443108'))

if __name__ == '__main__':
    test_orderQuery()