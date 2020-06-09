#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/9 8:53

'''
需求5-1：编写一系列条件测试，将结果的预测和实际结果都打印出来
'''

car = "subaru"
print("car == 'subaru'，I perdict True.")
print(car == 'subaru')

print("\ncar == 'audi',I perdict False.")
print(car == 'audi')

'''
需求5-2：检查两个字符串相等和不等
'''
strname1 = 'test01'
strname2 = 'test01'
strname3 = 'Test01'

print("strname1 == strnamr2, True")
print(strname1 == strname2)
print("\nstrname2 == strname3, Flase")
print(strname2 == strname3)
print("\nstrname1.lower() == strname3.lower(),True")

#使用函数lower()的测试
print(strname1.lower() == strname3.lower())  #lower()小写

#检查两个数字相等，不等，大于，小于，大于等于和小于等于
intname1 = 21
intname2 = 30
print("\n检查两个数字相等：{0}".format(intname1 == intname2))
print("\n检查两个数字不等：{0}".format(intname1 != intname2))
print("\n检查intname1大于intname2：{0}".format(intname1 > intname2))
print("\n检查intname1小于intname2：{0}".format(intname1 < intname2))
print("\n检查intname1大于intname2：{0}".format(intname1 >= intname2))
print("\n检查intname1小于intname2：{0}".format(intname1 <= intname2))

#使用关键字and测试,and前后条件要同时满足才是True,否则Fales
print("\n使用and关键字：{0}".format(intname1 >10 and intname2 <10))

#使用关键字or测试，or前后有一个条件满足就是True,两个条件都不满足是Fales
print("\n使用or关键字: {0}".format(intname1 >10 or intname2 <10))

#测试特定的值是否包含再列表中
list = [1,2,3,4,5,6,7,8]
print("\n检查数字10是否包含在list列表中：{0}".format(10 in list))
print("\n检查数字9未包含在list列表中：{0}".format(10 not in list))

'''
需求5-3：创建一个名为：alien_color的变量，并将其设置为："grenn"、"yellow"、"red"
'''
#编写if语句，检查外星人是否是绿色，如果是，打印一条消息，指出玩家获得5个点
alien_color = "green"
if alien_color == "green":
    print("\n我是绿色，恭喜你，获得5个点")

if alien_color != "rad":
    print("\n我是绿色，很遗憾，你错了！")

#使用if-else是绿色获得5个带你，不是绿色，获得10个点
if alien_color == "green":
    print("\n我是绿色，恭喜你，获得5个点")
else:
    print("\n我不是绿色，恭喜你，获得10个点")

#需求5-6：if-elif-else
age = 6
if age < 2 :
    print("\n他是婴儿")
elif age < 4:
    print("\n他正蹒跚学步")
elif age < 13:
    print("\n他是儿童")
elif age < 20:
    print("\n他是青少年")
elif age < 65:
    print("\n他是成年人")
else:
    print("\n他是老年人")

'''
需求5-8：创建一个至少5个用户的列表，其中一个为：admin，每次登录网站后都打印一条问候语，遍历每个用户
'''
current_users = ["jim","tom","jack","marry","mali","admin"]
#current_users = []
if current_users:
    for current_user in current_users:
        if current_user == "admin":
            print("\nHello admin , would you like to see a status report?")
        else:
            print("\nHello " + current_user + " , thank you for logging in again!")
else:
    print("\nWe need to find some users!")

'''
需求5-10：确保每位用户名都是独一无二的
'''
new_users = ["jim","kobe","TOM","gigi","jandon"]
for new_user in new_users:
    if new_user in current_users:
        print("\n您登录的用户名:" + new_user.lower() +" ,已被占用，请更改用户名。。。。")
    else:
        print("\n您登录的用户名:" + new_user.lower() +" ,未被占用，可以继续使用。。。。")

'''
需求5-11：序数表示位置，如1st和2nd,大多数序数都以th结尾，除1，2，3之外
'''
digital_lists = [0,1,2,3,4,5,6,7,8,9,10,11]
if digital_lists:
    for digital_list in digital_lists:
        if digital_list == 1:
            print("\n"+ str(digital_list) +"st")
        elif digital_list ==2 :
            print("\n"+ str(digital_list) +"nd")
        elif digital_list == 3:
            print("\n"+ str(digital_list) +"rd")
        else:
            print("\n"+ str(digital_list) +"th")
else:
    print("您需要的列表不能为空！")






