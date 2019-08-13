#!/usr/bin/env python
#_*_coding:utf-8_*_

import os

def getAllDirDE(path):

    stack = []
    stack.append(path)

    #处理栈，当栈为空的时候结束循环
    while len(stack) != 0:
        #从栈里取出数据
        dirPath = stack.pop()
        #print(dirPath)

        #目录下的所有文件
        filesList = os.listdir(dirPath)
        #print(filesList)

        #处理每一个文件，如果是普通文件则打印出来，如果是目录则将该目录的地址压栈
        for filesName in filesList:
            fileAbsPath = os.path.join(dirPath,filesName)
            if os.path.isdir(fileAbsPath):
                #是目录就压栈
                print("目录：" + filesName)
                stack.append(fileAbsPath)
            else:
                #普通文件就打印
                print("普通目录：" + filesName)

getAllDirDE(r"D:\Python\QFEDU\Day09\temp\dir")














