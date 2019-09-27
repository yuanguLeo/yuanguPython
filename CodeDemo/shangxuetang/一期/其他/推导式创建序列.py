#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/18 21:35

# 列表推导式
a = [i*2 for i in range(1,100) if i%9==0]
print(a)

# 使用普通的循环方式实现遍历元素
a2 = []
for i in range(1,5):
    a2.append(i)
print(a2)

b = [(row,col) for row in range(1,10) for col in range(1,10)]
print(b)
print("******************************")


# 字典推导式
'''
格式：
    {key:value for 表达式 in 可迭代对象}
注：字典推导式中可以增加if条件判断，多个for循环
'''
c = 'i love ptyhon , i love sxt , i love yuangu'
d = {d:c.count(d) for d in c}
print(d)

#使用普通方式统计字典中元素出现的次数
for d in c:
    c.count(d)
print(dict(d="c.count(d)"))
print("******************************")


# 集合推导式
e = {e for e in range(1,100) if e%9==0 }
print(e)
print("******************************")


# 生成器推导式（生成元组）
f = (f for f in range(1,100) if f%9==0)
print(tuple(f))
print(tuple(f))