#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/1 8:52
# 测试traceback模块的使用

import traceback

# 将异常信息输出到指定的文件中
try:
    print("step1")
    num = 10/0

except:
    with open(r"E:\123.txt","a") as f:  # a后面继续写，w是清空后在写
        traceback.print_exc(file=f)  # 输出异常
