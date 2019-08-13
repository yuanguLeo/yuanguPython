#!/usr/bin/env python
#_*_coding:utf-8_*_

import copy

def copyTtest():
    a = [10,20,[5,6]]
    b = copy.copy(a)

    print("打印原值a:",a)
    print("打印浅复制后的b:",b)

    b.append(30)
    b[2].append(7)
    print("********浅拷贝********")
    print("a:",a)
    print("b:",b)

def copyDeepTtest():
    a = [10,20,[5,6]]
    b = copy.deepcopy(a)

    print("打印原值a:",a)
    print("打印深复制后的b:",b)

    b.append(30)
    b[2].append(7)
    print("********深拷贝********")
    print("a:",a)
    print("b:",b)

copyTtest()
print("***********************")
copyDeepTtest()
