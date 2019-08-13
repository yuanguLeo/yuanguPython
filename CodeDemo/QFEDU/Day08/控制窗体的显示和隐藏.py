#!/usr/bin/env python
#_*_coding:utf-8_*_

import win32con
import win32gui
import win32api
import time

#找出窗体的编号
#QQwin = win32gui.FindWindow("TXGuiFoundation","QQ")

#隐藏窗体
#win32gui.ShowWindow(QQwin,win32con.SW_HIDE)

#显示窗体
#win32gui.ShowWindow(QQwin,win32con.SW_SHOW)

while True:
    QQwin = win32gui.FindWindow("TXGuiFoundation","QQ")
    win32gui.ShowWindow(QQwin,win32con.SW_HIDE)
    time.sleep(1)
    win32gui.ShowWindow(QQwin,win32con.SW_SHOW)
    time.sleep(1)

