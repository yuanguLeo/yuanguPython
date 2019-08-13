#!/usr/bin/env python
#_*_coding:utf-8_*_

#创建字典
a = {"name":"高小一","age":18,"salary":30000,"city":"北京"}
b = {"name":"高小二","age":19,"salary":20000,"city":"上海"}
c = {"name":"高小五","age":20,"salary":10000,"city":"深圳"}

#创建列表
tb = [a,b,c]

#获取第二行的人的薪资
print(tb[1].get("salary"))

#打印表中的所有薪资
for i in range(len(tb)):
    print(tb[i].get("salary"))

#获取所有的人的所有信息
for i in range(len(tb)):
    print(tb[i].get("name"),tb[i].get("age"),tb[i].get("salary"),tb[i].get("city"))