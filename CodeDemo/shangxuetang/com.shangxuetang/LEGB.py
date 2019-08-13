#!/usr/bin/env python
#_*_coding:utf-8_*_

#str = "name"

def outer():
    #str = "name"
    def inner():
        #str = "name"
        print(str)
    inner()
outer()
