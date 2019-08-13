#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019/7/25'

import tkinter


#创建主窗口
win = tkinter.Tk()

#设置标题
win.title("迪哥")

#设置大小和位置
win.geometry("600x600+200+20")

def showInfo():
    print(entry.get())

entry = tkinter.Entry(win)
entry.pack()


button = tkinter.Button(win, text = "按钮", command = showInfo)
button.pack()

win.mainloop()



