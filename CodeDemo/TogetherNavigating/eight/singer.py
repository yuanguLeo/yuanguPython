#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/17 11:26


'''
需求8-8：用户的专辑，用户自己输入歌手和专辑
'''
def make_album(singer_name,album_name):
    return {'singer_name':singer_name,'album_name':album_name}

while True:
    singer_name = input('请输入歌手名称：')
    if singer_name != 'q':
        album_name = input('请输入歌手专辑名称：')
        if album_name != 'q':
            c = make_album(singer_name,album_name)
            print(c)
            enter = input("是否继续填写？(y/n)")
            if enter == 'n':
                print('欢迎下次光临！')
                break
        else:
            print('欢迎下次光临！')
            break
    else:
        print('欢迎下次光临！')
        break

