#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
每一个模块都有一个__name__属性，当其值等于“__main__”时，
表明该模块自身在执行,否则被引入其他文件

当前文件如果为程序的入口文件，则__name__属性的值为__main__

'''

if __name__ == "__main__":
    print("这个leo模块")
else:

    def sayGood():
        print("leo is a good man!")

    def sayNice():
        print("leo is a nice man!")

    def sayHandsome():
        print("leo is a handsome man!")