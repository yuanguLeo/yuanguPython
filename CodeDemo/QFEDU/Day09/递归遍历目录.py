#!/usr/bin/env python
#_*_coding:utf-8_*_

import os

def getAllDirRE(path, sp = ""):
    #得到当前目录下所有的文件
    filesList = os.listdir(path)

    #处理每一个文件
    sp += "   "
    for filesName in filesList:
        fileAbsPath = os.path.join(path,filesName)
        #判断是否是路径（绝对路径）
        if os.path.isdir(fileAbsPath):
            print(sp + "目录：",filesName)
            #递归调用
            getAllDirRE(fileAbsPath,sp)
        else:
            print(sp + "普通文件：",filesName)

getAllDirRE(r"D:\Python\QFEDU\Day09\temp\dir")



















