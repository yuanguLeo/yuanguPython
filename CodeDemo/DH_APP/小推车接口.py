#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/19 9:43

import requests

def appDamo():

# 获取工作站接口
    url1 = 'http://192.168.55.99/?m=payorder&a=workstation'
    r1 = requests.get(url1)
    print(r1.url)
    print(r1.json())
    print("*********************************")

# 登陆接口
    url2 = 'http://192.168.55.99/?m=payorder&a=login'
    d2 = {"userName":"zd03","passWord":"zd03","userLoginAuth":"1","workStationId":"36"}
    r2 = requests.post(url2,params=d2)
    print(r2.url)
    print(r2.json())
    print("*********************************")

'''
#注销接口
    url3 = 'http://192.168.55.99/?m=payorder&a=loginOut'
    d3 = {"sessionId":""}
    r3 = requests.post(url3,data=d3)
'''


if __name__ == "__main__":
    appDamo()
