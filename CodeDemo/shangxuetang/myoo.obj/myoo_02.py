#!/usr/bin/env python
#_*_coding:utf-8_*_

class Student:

    company = "sxt"  #类属性
    count = 0 #类属性

    def __init__(self,name,score):
        self.name = name  #实例属性
        self.score = score
        Student.count = Student.count + 1

    def say_score(self): #实例方法
        print("我学Python的地方是：",Student.company)
        print("{0}的成绩是:{1}".format(self.name,self.score))

u1 = Student("张三",90) #u1是实例对象，自动调用__init__()方法
u1.say_score()

u2 = Student("李四",80)
u3 = Student("王五",100)
print("一共创建了{0}个Student对象".format(Student.count))