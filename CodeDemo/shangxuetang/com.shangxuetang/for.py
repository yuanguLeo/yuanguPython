#!/usr/bin/env python
#_*_coding:utf-8_*_

for i in "abcdef":
    print(i,end="\t")
print("\n")

for i in (10,20,30):
    print(i*30)
print("\n")

d = {"name":"张三","age":18,"job":"程序员"}

for i in d.keys():
    print(str("d.keys:")+i)
print("\n")

for i in d.values():
    print(i)
print("\n")

for i in d.items():
    print(i)
