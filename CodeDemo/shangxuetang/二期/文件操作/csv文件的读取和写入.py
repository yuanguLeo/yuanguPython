#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/14 9:11

# 测试csv文件的读取和写入

import csv

# 读取csv文件内容
with open(r"test.csv","r") as f:
    #a_csv = csv.reader(f)
    for row in  f:
        print(row)


# 写入csv文件内容
with  open(r"a.csv","w") as i:
    i_csv = csv.writer(i)
    i_csv.writerow(["ID","姓名","年龄"])
    i_csv.writerow(["1001","高小一","18"])
    a = [["1002","高小二","19"],["1003","高小五","20"]]
    i_csv.writerows(a)
