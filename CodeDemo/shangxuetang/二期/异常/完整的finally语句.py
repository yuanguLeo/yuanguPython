#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/31 9:48

try:
    f = open(r"E:\123.txt","r")
    content = f.readline()
    print(content)

except:
    print("文件未找到！")

finally:
    print("run in finally!")
    try:
        f.close()
    except BaseException as e:
        print(e)

print("程序结束。。。")
