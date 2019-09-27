#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/28 9:31

#二维列表

a = [["高小一",18,30000,"北京"],["高小二",19,20000,"上海"],["高小五",20,10000,"深圳"]]

print(a[0][0])


#遍历二维列表
for i in range(3):
    for x in range(4):
        print(a[i][x],end="\t")
    print()
