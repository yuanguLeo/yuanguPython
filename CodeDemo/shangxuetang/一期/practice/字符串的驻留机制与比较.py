#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/21 22:20

'''
驻留机制：符合python字符串条件时（仅包含下划线，字母数字），启动驻留机制
'''

# 例如1
a = "abc_123"
b = "abc_123"
print(a is b)
print(a == b)


# 例如2
c = "abc@"
d = "abc@"
print(c is d)  # ??python3.7的驻留机制与3.6不同？？
print(c == d)
print(id(c))
print(id(d))


'''
字符串的比较：is\not is
'''

print(a is b)
# print(a not is b)


'''
成员操作符: in 、not in 判断某个子字符串是否在字符串中
'''
e = "abcdefg"
print("b" in e)
print("bb" not in e)

