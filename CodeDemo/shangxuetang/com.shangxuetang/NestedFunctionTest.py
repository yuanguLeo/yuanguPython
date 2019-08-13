#!/usr/bin/env python
#_*_coding:utf-8_*_

def outer():
    print("outer")

    def inner():
        print("inner")

    inner()

outer()

def printChineseName(surname,name):
    print("{0}{1}".format(surname,name))

def printEnglishName(surname,name):
    print("{0}{1}".format(name,surname))


def printName(isChinese,surname,name):
    def inner_print(a,b):
        print("{0} {1}".format(a,b))

    if isChinese:
        inner_print(surname,name)
    else:
        inner_print(name,surname)

printName(True,"张","三")
printName(False,"Trump","Ivanka")
