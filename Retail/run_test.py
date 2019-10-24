#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/15 19:43

from login import *
import time

class TestRun():

    def runDemo(self):
        #登录集团版
        test_001 = Login("27612800","zd9455","zd9455")
        test_001.test_login()
        test_001.time(1)

        #进入卖品系统
        test_001.test_retail()
        test_001.time(1)

        #

