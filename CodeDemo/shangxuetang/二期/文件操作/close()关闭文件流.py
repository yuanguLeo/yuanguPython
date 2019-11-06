#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/6 9:05

try:
    a = open(r"a.txt","a")
    str = "yuangu"
    a.write(str)

except BaseException as e:
    print(e)

finally:
    a.close()

