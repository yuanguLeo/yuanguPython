#!/usr/bin/env python
#_*_coding:utf-8_*_

#参数的传递

a = [10,20]

print(id(a))
print(a)
print("***************")

def test01(m):
    print(id(m))
    m.append(30)
    print(id(m))

test01(a)
print(a)