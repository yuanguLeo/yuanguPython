#!/usr/bin/env python
#_*_coding:utf-8_*_

import time
import io

a = 'abcdefghijklmnopqrstuvwxyz'
print (a[2])


print (a.replace('c','张'))
print(a)


b = 'to be or not to be'
print(b[::-1])


#split()分割和 join()合并
a = "to be or no to be"
print(a.split())
print(a.split("be"))

a = ['sxt','sxt100','sxt200']
print('*'.join(a))

time01 = time.time()
for i in range (1000000):
    a += "abc"
time02 = time.time()
print ("+=所有时间为：" + str(time02 - time01))

time03 = time.time()
li= []
for i in range (1000000):
    li.append("abc")
a = "".join(li)
time04 = time.time()
print("join所有时间为：" + str(time04 - time03))


a = "我是:{0}，我的存款有:{1:.2f}万"
print(a.format("高琪",33.33))


b = '我是:{name},年龄是：{age}'
print(b.format(age = 19,name = "高琪"))

#左对齐
print("{:*>8}".format("245"))
#右对齐
print("{:*<8}".format("245"))
#居中
print("{:*^8}".format("245"))

#定义字符串
s = "Holle, sxt"
#创建一个新对象
sio = io.StringIO(s)
#打印新对象
print("sio等于："+str(sio))
#打印sio的内容
print(sio.getvalue())
#光标移动到索引为:7的元素
sio.seek(7)
#将7坐标对应值变为g
sio.write("g")
#打印
print(sio.getvalue())

print(list(range(10)))


a = [1,2,3,4,5,6]
print(id(a))
a.append(7)
print(a)

print(id(a))
#两个列表整合时，建议用extend，因为extend不会创建新对象
a.extend([10,20,30])
print(a)
print(id(a))
del a[0]
print(a)
a.insert(0,1)
print(a)






