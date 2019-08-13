#!/usr/bin/env python
#_*_coding:utf-8_*_

path = r"D:\Python\QFEDU\Day07\func1.txt"
with open(path,"wb") as f1:
    str = "leo is a good man迪"
    f1.write(str.encode("utf-8"))

with open(path,"rb") as f2:
    data = f2.read()
    print(data)
    #newData = data.decode("gdk")
    #print(newData)
    print(type(data))
