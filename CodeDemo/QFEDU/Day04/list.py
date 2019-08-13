#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
思考：要存储100个人的年龄
解决:使用列表
本质：是一种有序的集合

创建列表：
格式：列表名 = [列表选项1，列表选项2，。。。。。，列表选项n]
'''

#创建一个空列表
list1 = []
print(list1)

#创建带有元素的列表
list2 = [18,19,20,21,22]
print(list2)

#注意：列表中元素数据可以是不同类型的
list3 = [1,2,"sunck","good",True]
print(list3)

#列表元素的访问
#取值  格式：列表名[下标]
list4 = [1,2,3,4,5,6]
print(list4)
#替换
list4[2] = 300
print(list4)

#列表操作  组合
list5 = [1,2,3]
list6 = [5,6,7]
list7 = list5 + list6
print(list7)

#列表的重复
list8 = [1,2,3]
print(list8 * 3)

#判断元素是否在列表中
list9 = [1,2,3,4,5]
print(3 in list9)

#列表截取
list10 = [1,2,3,4,5,6,7,8,9]
print(list10[2:6])
print(list10[2:])
print(list10[:6])

#二维列表
list11 = [[1,2,3],[4,5,6],[7,8,9]]
print(list11[1][1])

#列表方法
#添加元素append 在列表的末尾添加新的元素
list12 = [1,2,3,4,5]
list12.append(6)
list12.append([7,8,9])
print(list12)

#extend 在末尾一次性追加另一个列表中的多个值
list13 = [1,2,3,4,5]
list13.extend([6,7,8])
print(list13)

#insert 在下标处添加一个元素，不覆盖原数据，原数据向后顺延
list14 = [1,2,3,4,5]
list14.insert(2,100)
list14.insert(2,[200,300])
print(list14)

#pop(x=lisrt[-1]) 移除列表中指定下标处的元素（默认移除最后一个元素），并返回删除的数据
list15 = [1,2,3,4,5]
list15.pop()
list15.pop(2)
print(list15.pop(1))
print(list15)

#remove 移除列表中的弄个元素第一个匹配的结果
list16 = [1,2,3,4,5,4,5,4]
list16.remove(4)
print(list16)

#clear 清楚列表中所有的数据
list17 = [1,2,3,4,5]
list17.clear()
print(list17)

#从列表中找出某个值第一个匹配的索引值
list18 = [1,2,3,4,5, 3,4,5,6]
index18 = list18.index(3)
print(index18)
#圈定范围
index19 = list18.index(3,3,7)
print(index18,index19)

#len列表中元素个数
list20 = [1,2,3,4,5]
print(len(list20))

#max 获取列表中的最大值
list21 = [1,2,3,4,5]
print(max(list21))

#min 获取列表中的最大值
list22 = [1,2,3,4,5]
print(min(list22))

#count 查看元素在列表中出现的次数
list23 = [1,2,3,4,5,3,4,5,3,3,5,6]
print(list23.count(3))
#删除列表中所有的3

num = 0
all = list23.count(3)
while num < all :
    list23.remove(3)
    num += 1
print(list23)

#reverse 倒序
list25 = [1,2,3,4,5]
list25.reverse()
print(list25)

#sort 升序
list26 = [2,1,4,3,5]
list26.sort()
print(list26)

#浅拷贝
list27 = [1,2,3,4,5]
list28 = list27
list28[1] = 200
print(id(list27))
print(id(list28))

#深拷贝
list29 = [1,2,3,4,5]
list30 = list29.copy()
list30[1] = 200
print(list29)
print(list30)
print(id(list29))
print(id(list30))

#将元组转成列表
list31 = list((1,2,3,4))
print(list31)
