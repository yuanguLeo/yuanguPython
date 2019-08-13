#!/usr/bin/env python
#_*_coding:utf-8_*_

def test01(n):
    if n==0:
        print("over")
    else:
        test01(n-1)
    print(n)

test01(4)