#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/10/26 17:08

'''
第三课：插曲之变量和字符串
'''

#测试题：

#0. 以下哪个变量的命名不正确？为什么？

    #(A) MM_520  (B) _MM520_  (C) 520_MM  (D) _520_MM
#C ,因为python不能用数字开头


#1. 在不上机的情况下，以下代码你能猜到屏幕会打印什么内容吗？
#>>>myteacher = '小甲鱼'
#>>>yourteacher = myteacher
#>>>yourteacher = '黑夜'
#>>>print(myteacher)

#打印小甲鱼

#2. 在不上机的情况下，以下代码你能猜到屏幕会打印什么内容吗？
# myteacher = '小甲鱼'
# # yourteacher = myteacher
# # myteacher = '黑夜'
# # print(yourteacher)

#小甲鱼


#3. 在不上机的情况下，以下代码你能猜到屏幕会打印什么内容吗？
# first = 520
# second = '520'
# first = second
# print(first)

#520

# 4. 除了使用反斜杠（\）进行字符转义，还有什么方法可以打印：Let's go! 这个字符串？
#print("Let's go!")

# 5. 如果非要在原始字符串结尾输入反斜杠，可以如何灵活处理？
print("123'\\'")

# 6. 在这一讲中，我们说变量的命名需要注意一些地方，但小甲鱼在举例的时候貌似却干了点儿“失误”的事儿，你能看得出小甲鱼例子中哪里有问题吗？


# 动动手：

# 0. 还记得我们第一讲的动动手的题目吗？这一次要求使用变量，计算一年有多少秒？
# 提示：可以以 DaysPerYear（每年天数），HoursPerDay（每天小时数），MinutesPerHour（每小时分钟数），SecondsPerMinute（每分钟秒数）为变量名。
DaysPerYear = 365
HoursPerDay = 24
MinutesPerHour = 60
SecondsPerMinute = 60
print(SecondsPerMinute * MinutesPerHour * HoursPerDay * DaysPerYear)

# 1. 关于最后提到的长字符串（三重引号字符串）其实在 Python3 还可以这么写，不妨试试，然后比较下哪种更方便？

# >>> string = (
# "我爱鱼C，\n"
# "正如我爱小甲鱼，\n"
# "他那呱唧呱唧的声音，\n"
# "总缠绕于我的脑海，\n"
# "久久不肯散去……\n")

string = '''
"我爱鱼C，\n"
"正如我爱小甲鱼，\n"
"他那呱唧呱唧的声音，\n"
"总缠绕于我的脑海，\n"
"久久不肯散去……\n"
'''

# 2. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
#学的了变量，input和if、else等BIF

