#!/usr/bin/env python
#_*_coding:utf-8_*_

from PIL import Image

'''
Pillow  非常强大的处理图像的工具库
pip install Pillow
Windows安装如果报错，则输入：pip install --upgrade pip  升级pip

'''

#打开图片
im = Image.open("2014.jpg")
#查看图片的信息
print(im.format, im.size, im.mode)























