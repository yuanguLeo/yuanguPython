#!/usr/bin/env python
#_*_coding:utf-8_*_

class Person(object):

    def __init__(self,gun):
        self.gun = gun

    def fire(self):
        self.gun.shoot()

    def fillBullet(self,count):
        self.gun.bulletBox.bulletCount = count




