#!/usr/bin/env python
#_*_coding:utf-8_*_

#推导式练习
#列表推导式
y = [i*2 for i in range(1,5)]
print(y)

y = []
for i in range(1,5):
    y.append(i*2)
print(y)

cells = [(row,col) for row in range(1,10) for col in range(1,10)]
print(cells)

#字典推导式
my_text = 'i love you, i love sxt, i love zhangsan'
my_count = {c:my_text.count(c) for c in my_text}
print(my_count)

#集合推导式
b = {i for i in range(1,100) if i%9==0}
print(b)

#生成器推导式，生成元组 tuple生成元组
#a 是生成器对象，生成器对象也是可迭代的
a = (i for i in range(1,100) if i%3==0)
print(tuple(a))
#一个生成器对象只能运行一次，第一次迭代可以得到数据，第二次迭代发现数据已经没有了
print(tuple(a))
