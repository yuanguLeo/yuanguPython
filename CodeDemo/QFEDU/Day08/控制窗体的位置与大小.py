#!/usr/bin/env python
#_*_coding:utf-8_*_

import win32con
import win32gui
import random

QQwin = win32gui.FindWindow("TXGuiFoundation","QQ")

#参数1：控制的窗体
#参数2：大致方位
#参数3：位置x
#参数4：位置y
#参数5：长度
#参数6：宽度
#win32con.SWP_SHOWWINDOW   一直显示
#win32gui.SetWindowPos(QQwin,win32con.HWND_TOPMOST,100,100,300,300,win32con.SWP_SHOWWINDOW)

while True:

    x = random.randrange(900)
    y = random.randrange(600)
    win32gui.SetWindowPos(QQwin,win32con.HWND_TOPMOST,x,y,300,300,win32con.SWP_SHOWWINDOW)


