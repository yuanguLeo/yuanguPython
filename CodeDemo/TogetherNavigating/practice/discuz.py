#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 8:40

'''
python向mysql数据库中插数据
'''

import pymysql
# 打开数据库连接
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='huice30', charset='utf8')
# 使用cursor()方法获取操作游标
cursor=db.cursor()

try:
    i = 1
    while i <= 200:
       prefix = "zdtest"
       data = (prefix+str(i),prefix+str(i),prefix+str(i)+'@qq.com')
       #sql语句
       sql = "insert into user(username,password,email) values('%s','%s','%s');"%(data)
       #执行sql
       cursor.execute(sql)
       #提交到数据库
       db.commit()
       i += 1;
       print(data)
       print('执行完毕！')
except:
    print("sql语句出错了！")
    db.rollback()

#关闭游标
cursor.close()
#关闭数据库
db.close()

