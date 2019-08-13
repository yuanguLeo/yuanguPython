#!/usr/bin/env python
#_*_coding:utf-8_*_


import pickle   #数据持久性模块

myList = [1,2,3,4,5,"leo is a good man"]
path = r"D:\Python\QFEDU\Day08\func1.txt"

f = open(path, "wb")
pickle.dump(myList,f)
f.close()

#读取
f1 = open(path,"rb")
pickle.load(f1)
print(myList)
f1.close()



















