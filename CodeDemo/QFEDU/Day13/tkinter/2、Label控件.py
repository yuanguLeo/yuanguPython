#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019/7/23'


import tkinter

win = tkinter.Tk()
win.title("迪哥")
win.geometry("600x600+200+20")

'''
Label       标签控件可以显示文本
text        显示的文本内容
bg          背景色
fg          字体颜色
wraplength  指定text文本中多宽进行换行
justify     设置换行后的对齐方法
anchor      n北，e东，s南，w西，center居中 ne se sw nw
'''

label = tkinter.Label(win,text = "leo",
                          bg = "blue",
                          fg = "red",
                          font = ("黑体",20),
                          width = 10,
                          height = 4,
                          wraplength = 300,
                          justify = "left",
                          anchor = "n",   #默认center居中

                            )

#显示出来
label.pack()


win.mainloop()
