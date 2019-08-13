#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
需求：打印如下图案
        0 0 0 0 0
        1 1 1 1 1
        2 2 2 2 2
        3 3 3 3 3
        4 4 4 4 4
'''

for i in range(5):
    for x in range(5):
        print(i,end='\t')
    print()
print("****************************")
print()
'''
需求：利用嵌套循环打印九九乘法表
'''

sum = 0
for i in range(1,10,1):
    for x in range(1,i+1,1):
        print("{0}*{1}={2}".format(i,x,(i*x)),end="\t")
    print()



