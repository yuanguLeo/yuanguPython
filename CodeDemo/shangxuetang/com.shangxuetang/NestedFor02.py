#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
需求：用列表和字典存储下表信息，并打印出表中工资高于15000的数据
        姓名      年龄      薪资        城市
        高小一     18      30000       北京
        高小二     19      20000       上海
        高小五     20      10000       深圳
'''

#创建字典
a = {'name':'高小一','age':18,'salary':30000,'city':'北京'}
b = {'name':'高小二','age':19,'salary':20000,'city':'上海'}
c = {'name':'高小五','age':20,'salary':10000,'city':'深圳'}

#创建列表
tb = [a,b,c]

for i in tb:
    if (i.get("salary")>15000):
        print(i)