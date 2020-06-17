#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/16 14:42

'''
需求8.1例题
'''
def greet_user():
    '''显示问候语'''
    print('hello, Python! ')

greet_user()

'''
需求8-1：display_message()的函数，打印一句话
'''
def display_message(username):  #括号里面的是形参
    '''练习def定义函数'''
    print('\nhello, '+ username)

display_message('tom')  #调用传递的是实参

'''
需求8-2：喜欢的图书
'''
def favorite_book(title):
    print('\nOne of my favorite books is ' + title)

favorite_book('Alice in Wonderland')

'''
需求8-3：编写一个名为：make_shirt()的函数，接受一个尺码和T恤上要印的字样
'''
def make_shirt(size,pattern):
    print('\n我需要'+size+'码的T恤，要印'+pattern+'图案')

make_shirt('ss','篮球')
make_shirt(size = 'xl',pattern = 'jondan')

'''
需求8-4：大号T恤，修改函数make_shirt(),在默认值情况下，印“I love python”
'''
def make_shirt(size,pattern='I lova python!'):
    print('\n我需要'+size+'的T恤，要印'+pattern+'图案')

make_shirt('大号')
make_shirt('中号')
make_shirt('小号','start python')

'''
需求8-5：编写一个名为describe_city()的函数，接受一座城市的名字和该城市所以属国家
'''
def describe_city(city,countries='china'):
    print('\n'+city+' is in '+countries)

describe_city('beijing')
describe_city('shanghai')
describe_city('yanqin','beijing')

'''
需求8-6：编写city_country()的函数，并返回
'''
def city_country(city,country):
    return ('\n'+city+' , '+country)
    #return  {'city': city,'country':country}
massage = city_country('北京','中国')
print(massage)

'''
需求8-7：make_album()函数，创建一个描述音乐专辑的字典，接受歌手和专辑名，打印返回值
'''
def make_album(singer_name,album_name,singer_number=' '):
    if singer_number:
        return {'singer_name':singer_name,
                'album_name':album_name,
                'singer_number':singer_number}
    else:
        return {'singer_name':singer_name,'album_name':album_name}
a = make_album('许巍','无尽光芒')
print(a)

b = make_album('赵雷','无法长大','10首歌曲')
print(b)

'''
需求8-9：魔术师
'''
def show_magician(name_lists):
    for name_list in name_lists:
        print('\n需求8-9： '+ name_list +'hello!')

name_lists = ['西里尔·高山','刘谦','杰森·拉蒂']
show_magician(name_lists)


'''
需求8-10：编写一个make_great()的函数，在每个魔术师的名字中都加入字样“the Great”,
调用show_magician,确实列表变了
'''
def show_magician(name_lists):
    for name_list in name_lists:
        print('\n需求8-10： ' + name_list + 'hello')

def make_great(name_lists):
    n = 0
    while n < len(name_lists):
        name_lists[n] = '\n需求8-10： the Great'+ name_lists[n]
        n += 1

    show_magician(name_lists)

name_lists = ['西里尔·高山','刘谦','杰森·拉蒂']
make_great(name_lists)

'''
需求8-11：
'''
def show_magician(name_lists,new_name_lists):
    while name_lists:
        name_list = name_lists.pop()
        print('\n需求8-11： ' + name_list + ',hello!')
        new_name_lists.append(name_list)

def make_greats(name_lists):
    n = 0
    while n < len(name_lists):
        name_lists[n] = 'the Great'+ name_lists[n]
        n += 1
    show_magician(name_lists,new_name_lists)

name_lists = ['西里尔·高山','刘谦','杰森·拉蒂']
new_name_lists = []

show_magician(name_lists[:],new_name_lists)
make_greats(name_lists)








