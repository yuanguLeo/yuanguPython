#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/17 21:51

'''
continue:结束本次循环，进行下一次循环

'''

# 需求：输入员工的薪资，若薪资小于0则重新输入，最后打印出录入员工的数量和薪资明细，以及平均薪资

empNum = 0
salarySum = 0
salarys = []

while True:
    a = input("请输入您的薪资：")

    if a.upper() == "Q":
        print("输入结束,退出！")
        break

    if float(a) < 0:
        continue

    empNum += 1
    salarys.append(float(a))
    salarySum += float(a)

print("员工数为:{0}人".format(empNum))
print("薪资明细为：",salarys)
print("平均薪资为：{0}".format(salarySum/empNum))


