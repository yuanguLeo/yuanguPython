#!/usr/bin/env python
#_*_coding:utf-8_*_

class Gun(object):

    def __init__(self,bulletBox):
        self.bulletBox = bulletBox

    def shoot(self):
        if self.bulletBox.bulletCount == 0:
            print("没有子弹了")
        else:
            self.bulletBox.bulletCount -= 1
            print("剩余子弹为：%d发" % (self.bulletBox.bulletCount))















