#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
for 语句

格式：
for 变量名 in 集合：
    语句

逻辑：按顺序取“集合”中的每一个元素赋值给“变量”，再去执行语句。如此循环往复，直到取完“集合”中的元素截止

'''

for i in [1,2,3,4,5]:
    print(i)

'''
range([start,] end [, step])函数  列表生成器
start默认为0.step默认为1
功能：生成数列

'''
for i in range (100):
    print(i)


#同时便利下标和元素

for index , m in enumerate([1,2,3,4,5]): #index,m = 下标，元素
    print(index,m)

#需求：使用for循环实现：1+2+3+4+.....100的和

sum = 0
for i in range (101):
    sum += i
print(sum)

'''
break语句：
作用：跳出for和while循环
注意：只能跳出距离它最近的那一层循环
'''

for i in range(10):
    print(i)
    if i == 5:
        break

num = 1
while num <= 10:
    print(num)


    if num == 3:
        break
    num += 1
'''
注意：循环语句可以有else语句，break导致循环截止，不会执行else下面的语句

'''
#else:  #不会执行
 #   print("leo is a good man")

'''
continue语句
作用：跳过当前循环中的剩余语句，然后继续下一次循环
注意：跳过距离最近的循环
'''

for i in range (10):
    print(i)
    if i == 3:
        continue
    print("*")
    print("&")