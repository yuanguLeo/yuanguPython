#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019/7/23'

import tkinter


#创建主窗口
win = tkinter.Tk()

#设置标题
win.title("迪哥")

#设置大小和位置
win.geometry("600x600+200+20")

'''
输入控件
用于显示简单的文本内容
show 密文显示 show = "*"
'''

#绑定变量
e = tkinter.Variable()
entry = tkinter.Entry(win, show = "*" , textvariable = e)
entry.pack()

#e就代表输入框这个对象
#设置值
e.set("yuanguleo is a good man")


#取值
print(e.get())
print(entry.get())

win.mainloop()
