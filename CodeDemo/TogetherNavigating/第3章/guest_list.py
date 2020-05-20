#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 17:40

'''
需求3-4：创建3人的嘉宾名单
'''

guest = ['许巍','周杰伦','孙燕姿']
print("赴约嘉宾名单为：{0}".format(guest))

'''
需求3-5：有嘉宾无法赴约，需换人
'''
del_guest = guest.pop(1)
print(del_guest+"：因为工作原因不能赴约！")
guest.append('谢天笑')
print("新赴约嘉宾名单改为：{0}".format(guest))

'''
需求3-6：添加嘉宾3位
'赵雷','陈粒','任贤齐'
'''
guest.append("赵雷")
guest.append('陈粒')
guest.append('任贤齐')
print("更大的餐桌可容纳：{0}".format(guest))

#用insert再开头增加一个人
guest.insert(0,'李荣浩')
print("查看最后的名单：{0}".format(guest))

#用insert将一个人添加到名单中间
guest.insert(3,'朴树')
print("添加到中间后，名单变为：{0}".format(guest))

#使用append将最后一个名单添加到最后
guest.append('大张伟')
print("名单为：{0}".format(guest))

'''
需求3-7：缩减名单至两人
'''
pop_guset = guest.pop()
pop_guset = guest.pop()
pop_guset = guest.pop()
pop_guset = guest.pop()
pop_guset = guest.pop()
pop_guset = guest.pop()
pop_guset = guest.pop()
print("目前剩余的两人是：{0}".format(guest))

#使用del将最后两人删除
del guest[1]
del guest[0]
print("目前的人名单为：{0}".format(guest))

'''
需求3-8：想出至少5个渴望去旅游的地方
'''

add = ['changlong','chengdu','chongqing','xizang','xinjiang']
print(add)

#使用sorted()按字母顺序打印列表
print("\n使用sorted()按字母顺序打印列表: ")
print(sorted(add))

#再次打印列表，核实顺序未变
print("\n再次打印列表，核实顺序未变: ")
print(add)

#使用sorted()按与字母顺序相反的顺序打印这个列表,reverse=True反序
print("\n使用sorted()按与字母顺序相反的顺序打印这个列表,reverse=True反序: ")
print(sorted(add,reverse=True))

#使用reverse反转列表
print("\n使用reverse反转列表: ")
add.reverse()
print(add)

#使用sort()改变列表顺序
print("\n使用sort()改变列表顺序: ")
add.sort()
print(add)

#使用sort()改变列表顺序后，再次反转
print("\n使用sort()改变列表顺序后，再次反转: ")
add.sort(reverse=True)
print(add)

#需求3-9：计算列表长度
print("\n计算列表长度为：{0}".format(len(add)))

#需求3-11：有意引发一个错误
#print(add[5])

#每次返回列表中的最后一个值
print("\n打印add列表值：{0}".format(add))
print("每次返回列表中的最后一个值: "+add[-1])


