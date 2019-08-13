#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
需求：输入员工的薪资，若薪资小于0则重新输入，最后打印出录入员工的数量和薪资明细，以及平均薪资
'''

#记录员工数
empNum = 0
#记录薪资总数
salarySum = 0
#记录薪资明细
salays = []

while True:
    a = input("请输入员工的薪资(如果输入Q或q，就退出)：")
    if (a=="Q" or a=="q"):
        print("循环结束，退出")
        break
    if (float(a)<0):
        continue

    empNum  += 1
    salays.append(float(a))
    salarySum += float(a)

print("员工数为{0}：".format(empNum))
print("薪资为{0}：".format(salays))
print("平均薪资为{0}：".format(salarySum/empNum))