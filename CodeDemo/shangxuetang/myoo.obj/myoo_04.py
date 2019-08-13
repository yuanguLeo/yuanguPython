#!/usr/bin/env python
#_*_coding:utf-8_*_

#测试析构方法 __del__

class Person:

    def __del__(self):
        print("销毁对象{0}".format(self))

p1 = Person()
p2 = Person()

del p2
print("程序结束")