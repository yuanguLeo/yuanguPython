#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/16 10:52

'''
需求7-8：创建一个名为：sandwich_orders列表，创建包含各种三明治的名字，在创建一个名为：
finished_sandwinches的空列表，遍历sandwich_orders，将其移到列表finished_sandwinches中
'''
sandwich_orders = ['tuna_sandwich','chicken_sandwich','beef_sandwich']
finished_sandwinches = []
sandwich_order = 0
if sandwich_orders != []:
    while sandwich_orders:
        finished_sandwinches.append(sandwich_orders.pop())
        print('I made your '+ finished_sandwinches[sandwich_order] )
        sandwich_order += 1
print(finished_sandwinches)

'''
需求7-9：确保pastrami在sandwich_orders列表中至少出现三次，pastrami卖完了，使用while循环
将sandwich_orders中的pastrami都删除，打印列表不包含pastrami
'''
sandwich_orders = ['pastrami','tuna_sandwich','pastrami','chicken_sandwich','pastrami','beef_sandwich']

print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print('卖完pastrami之后的sandwich_orders列表：{0}'.format(sandwich_orders))

'''
需求7-10：编写一个程序，调查用户梦想的度假胜地，使用类似于'If you could cisit one place 
in the world,where would you go ?'的提示，并编写一个打印调查结果的代码块
'''
responses = {}
polling_active = True
while polling_active:
    name = input('\n what are you name?')
    response = input('If you could cisit one place in the world,where would you go ?')
    responses[name] = response
    repeat = input('Do you want to continue?(yes/no)')
    if repeat == 'no':
        polling_active = False
print(responses)



