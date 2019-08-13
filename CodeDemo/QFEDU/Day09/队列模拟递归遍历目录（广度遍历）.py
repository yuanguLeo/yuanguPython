#!/usr/bin/env python
#_*_coding:utf-8_*_

import os
import collections

def getAllDirQU(path):
    #创建队列
    queue = collections.deque()
    #进队列
    queue.append(path)

    while len(queue) != 0:
        #出队列
        dirPath = queue.popleft()
        #找出所有文件
        filesList = os.listdir(dirPath)

        for filesName in filesList:
            #合成绝对路径
            fileAbsPath = os.path.join(path,filesName)

            if os.path.isdir(fileAbsPath):
                print("目录：" + filesName)
                queue.append(fileAbsPath)
            else:
                print("普通文件：" + filesName)


getAllDirQU(r"D:\Python\QFEDU\Day09\temp\dir")













