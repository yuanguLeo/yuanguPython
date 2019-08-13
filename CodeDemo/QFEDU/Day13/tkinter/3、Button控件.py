#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019/7/23'


import tkinter

def func():
    print("yuanguleo is a good man")

#创建主窗口
win = tkinter.Tk()

#设置标题
win.title("迪哥")

#设置大小和位置
win.geometry("600x600+200+20")

#创建按钮
button1 = tkinter.Button(win, text = "按钮", command = func, width=10, height=10)
button1.pack()

button2 = tkinter.Button(win, text = "按钮", command = lambda : print("yuanguleo is a nice man"))
button2.pack()

button3 = tkinter.Button(win, text = "按钮", command = win.quit)
button3.pack()

win.mainloop()
