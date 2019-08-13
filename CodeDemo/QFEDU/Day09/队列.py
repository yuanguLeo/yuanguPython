#!/usr/bin/env python
#_*_coding:utf-8_*_

import collections

#创建队列  队列先进先出
queue = collections.deque()
print(queue)

#进队列
queue.append("A")
queue.append("B")
queue.append("C")
print(queue)

#出队列
res1 = queue.popleft()
print(res1)
print(queue)
res2 = queue.popleft()
print(res2)
print(queue)
res3 = queue.popleft()
print(res3)
print(queue)













