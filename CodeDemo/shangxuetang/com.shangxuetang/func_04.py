#!/usr/bin/env python
#_*_coding:utf-8_*_

import time
import math

def test01():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print("test01()耗时为：{0}".format((end-start)))

def test02():
    a = math.sqrt
    start = time.time()
    for i in range(10000000):
        a(30)
    end = time.time()
    print("test02()耗时为：{0}".format((end-start)))


test01()
test02()
