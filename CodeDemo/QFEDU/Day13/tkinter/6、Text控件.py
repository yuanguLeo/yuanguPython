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

'''
文本控件，用于显示多行文本

'''

text = tkinter.Text(win, width = 30, height = 4)
text.pack()

str = '''dfkskjfjskjfisljfowejoiwjoifjslkfjslkdjfklsjflksjflksjdfklsdjfkljsdklfjskl
jfsdklfjslkdjfklsdjfklsdjfkldjfklsdjfkljoiewjiowuiofjsdfdkljfkdslfjksldfjklsdjflksdjflk
jkdlsjflkdsjfkldjflkdsjfkldsjflksdjfkldjfklsdjfklsdjfkldjflksdjflksdjflksjlkdsjflksjflsd
jflkdjflksdfjlkdjflkdsjfkldsjflkdjfslkdjflkdjflkdjflkdsjflksjflksjlwjfljlfjldsfjkdslfjkds
jfdklfjklsdjfkldsjfldjfkldjfkdjfkdjfklsdjfkdjfkldjkfdjfkldjfkldjfkdjfkldsjfkdjfkdjfdkljf'''

text.insert(tkinter.INSERT , str)


win.mainloop()
