#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/12 18:22

'''
数据库配置
'''

import pymysql

# 旧数据库
conn_old = pymysql.connect(host="172.16.1.210",
                           user="root",
                           password="123456",
                           db="center",
                           port=3306,
                           ) #charset="utf8"
# 新数据库
conn_new = pymysql.connect(host="172.16.1.203",
                           user="test",
                           password="cine123456",
                           db="dgp_membership_db",
                           port=3306,
                           ) #charset="utf8"


