#!/usr/bin/env python
#_*_coding:utf-8_*_

#创建对象和调用对象

class student: #类名一般首字母大写，多个单词采用驼峰原则
    def __init__(self,name,score): #self必须是第一个参数   构造方法格式：__init__()
        self.name = name
        self.score = score

    def say_score(self): #self必须是第一个参数
        print("{0}的分数是：{1}".format(self.name,self.score)) #每个参数前面都要加self

s1 = student("张三",100) #通了类名()调用构造函数。执行了两个步骤： 1、__new__()方法创建对象 2、__init__()方法初始化创建好的对象，给实例属性赋值
s1.say_score()
student.say_score(s1)