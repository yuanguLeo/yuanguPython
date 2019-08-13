#!/usr/bin/env python
#_*_coding:utf-8_*_

path  = r"D:\Python\QFEDU\Day07\func.txt"
f = open(path,"w")

#写文件
#1、将信息写入缓冲区
f.write("leo is a good man!")

#2、刷新缓冲区
#直接把内部缓冲区的数据立刻写入文件，而不是被动的等待自动刷新缓冲区写入
f.flush()

f.close()