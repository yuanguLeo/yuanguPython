#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
概述：
使用键-值（key-value）存储，具有极快的查找速度

注意：字典是无序的

key的特性：
1、字典中的key必须唯一
2、key必须是不可变对象
3、字符串、整数等都是不可变的，可以作为key
4、list是可变的，不能作为key

思考：保存多位学生的姓名与成绩

使用字典，学生姓名为key，学生成绩作为值



'''

dict1 = {"tom":60,"lilei":70}
#元素的访问
#获取：字典名[key]
print(dict1["lilei"])
#print(dict1["leo"])  #没有找到leo的成绩

print(dict1.get("leo"))


#添加
dict1["hanmeimei"] = 99
#因为一个key对应一个value，所以，多次对一个key的value赋值，其实就是修改
dict1["lilei"] = 80
print(dict1)

#删除
#dict1.pop("tom")
#print(dict1)


#遍历
for key in dict1:
    print(key,dict1[key])

print("**************")
print(dict1.values())
for value in dict1.values():
    print(value)


print("**************")
print(dict1.items())
for x , y in dict1.items():
    print(x , y)

print("**************")
#枚举法
print(enumerate(dict1))
for k , l in enumerate(dict1):
    print(k , l)


#字典和list比较
#1、查找和插入的速度极快，不会随着key-value的增加而变慢
#2、需要占用大量的内存，内存浪费多

#list
#1、查找和插入的速度随着数据量的增多而减慢
#2、占用空间小，浪费内存少

'''
练习：

str = “leo is a good man! leo is a good man! leo is a good man! leo is a good man! leo is a good man! leo is a good man! leo is a good man! leo is a good man! leo is a good man!”

分析过程：
1、以空格切割字符串
2、循环处理列表中的每一个元素
3、以元素当做key去一个字典中提取数据
4、如果没有提取到，就以该元素作为key,1作为value，存进字典
5、如果提取到，将对应的key的value修改，值加1
6、根据输入的字符串当做key再去字典取值

'''