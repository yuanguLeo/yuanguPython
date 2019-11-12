#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/12 9:00

with open("2014.jpg","rb") as f:
    with open("2014_copy.jpg","wb") as w:
        for line in f.readlines():
            w.write(line)

print("拷贝完成。。。")
