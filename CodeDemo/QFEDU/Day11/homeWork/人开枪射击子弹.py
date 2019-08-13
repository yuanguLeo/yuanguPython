#!/usr/bin/env python
#_*_coding:utf-8_*_

from person import Person
from gun import Gun
from bulletbox import BulletBox



'''
需求：人开枪射击子弹，用面向对象思想写一段代码

分析：

人
类名：Person
属性：gun
行为：fire

枪
类名：Gun
属性：bulletBox
行为：fire

弹夹
类名：BulletBox
属性：bulletCount
行为：

'''

#创建弹夹
bulletbox = BulletBox(5)

#创建枪
gun = Gun(bulletbox)

#人
per = Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()

per.fillBullet(2)
per.fire()
per.fire()
per.fire()










