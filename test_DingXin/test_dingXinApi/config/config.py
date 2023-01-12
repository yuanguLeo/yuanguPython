#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/1/10 15:30

'''
配置文件
'''

ip = '172.16.3.111'
http_ip = 'http://'+ ip
name = 'inner'
password = 'SnAw19sKd34n'

def sql_conf():
    '''
        host数据库ip
        user数据库用户名
        password数据库密码
        database:连接数据库名
        port数据库端口
        chrset数据库字符集 中文utf-8
        :return:
        '''
    host = ip
    # user = 'test'
    # password = 'cine123456'
    user = 'test'
    password = 'cine123456'
    database = 'mysql'
    port = 3306
    charset = 'utf8'  # 这用utf8，utf-8会报错
    return host, user, password, database, port, charset

