#!/usr/bin/env python
#_*_coding:utf-8_*_

from collections import Iterable
from collections import Iterator

'''
可迭代对象：可以直接作用于for循环的对象，统称为：可迭代对象（Iterable）.
可以用isinstance()去判断一个对象是否是Iterable对象

可以直接作用于for的数据类型一般分两种：
1、集合数据类型，如：list、tuple、dict、set、seting
2、是generator，包括生成器和带yield的是generator function


迭代器：不但可以作用于for循环，还可以被next()函数不断的调用，并返回下一个值，
直到最后跑出一个StopIteration错误表示无法继续返回下一个值


可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator对象)
可以使用isinstance()函数判断一个对象是否是Iterator对象


'''

print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance("",Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(1,Iterable))


print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance("",Iterator))
print(isinstance((x for x in range(10)),Iterator))

