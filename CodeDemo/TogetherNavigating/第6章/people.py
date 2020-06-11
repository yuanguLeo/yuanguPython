#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/10 10:51

'''
需求6-1：使用字典来存储一个人的信息，包括名，姓，年龄，居住城市
'''
peoples_ditc = {"surname":"张","name":"二狗","age":18,"city":"北京"}
print(peoples_ditc)
print("张二狗的年龄是："+str(peoples_ditc["age"]) + "岁。")

#需求6-2：想出5个人名，作为字典的键，想出每个人喜欢的数字，将这些数字作为值存储在字典中
peoples_dict = {"王大":5,"赵二":6,"张三":8,"李四":9,"王五":3}
print(peoples_dict)

#需求6-3：词汇表，写出5个python的词汇
python_vocabulary = {
    "Code lay out":"代码布局",
    "Whitespaces in Expressions":"表达式中的空格",
    "Comments":"注释"
}
print(python_vocabulary)
python_vocabulary["Naming Conventions"] = "命中规则"
python_vocabulary["Programming recommendatetions"] = "编程建议"
print(python_vocabulary)
print(python_vocabulary.keys())
print(python_vocabulary.values())


''''
90页：例题
'''
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
friends = ["phil","sarah"]
for name in favorite_languages:
    print('\n'+name.title())

    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is "
              + favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")

'''
需求6-4：将6-3的练习使用for循环遍历，之后再增加5个术语，再次运行
'''
for word,explaination in python_vocabulary.items():
    print("\n"+ word +"：")
    print(explaination)

python_vocabulary["Global Variable Names"] = "全局变量名"
python_vocabulary["Function Annotation"] = "功能注释"
python_vocabulary["Indentation"] = "缩进"
python_vocabulary["Binary Operator"] = "运算符"
python_vocabulary["String quotes"] = "字符串引号"
for key, value in python_vocabulary.items():
    print("\n" + key + " :")
    print(value)

'''
需求6-5：河流，创建一个字典，其中储存三条大河流及其流经的国家，其中一个键-值对可能是nile,egypt
'''
rivers = {"Yellow River":"China","Amazon River":"Colombia","Nile":"Egypt"}
#使用循环打印The Nile runs through Egypt
for key,vlaue in rivers.items():
    print("\nThe " + key + " runs through " + vlaue)

#使用循环打印河流名称
for river_key in rivers.keys():
    print('\n河流名称： '+river_key)

#使用河流打印国家名称
for river_vlaue in rivers.values():
    print('\n河流经过的国家名称： '+river_vlaue)

'''
需求6-6：在6.3.1节编写的程序favoite_languages.py中执行以下操作
'''
#创建一个应该会接受调查的人员名单，其中有些人已经包含在字典中，而其他人没包括
# favorite_languages = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python',
# }

name_lists = ['jen','jim','tom','edward']

#被调查的打印调查结果，没有调查的，打印一条邀请参与调查
for name_list in name_lists:
    if name_list in favorite_languages.keys():
        print('\nHi , '+ name_list +
              ' I see yuor favorite language is ' +
              favorite_languages[name_list])
    else:
        print("\n"+name_list + " ,please take our poll!")

'''
6.4.2例题
'''
#存储所点披萨的信息
pizza = {
    'crust':'thick',
    'topping':['mushrooms','extra cheese'],
}

#概述所点的披萨
print('\nYou ordered a '+ pizza['crust'] +"-crust pizza "
      +'with the follwing toppings:')

for topping in pizza['topping']:
    print('\t' + topping)

'''
需求6-7：
'''
peoples1= {
    "surname":"张三",
    "city":"北京",}

peoples2 = {
    "surname":"李四",
    "city":"上海",}

peoples3 = {
    "surname":"王五",
    "city":"广州",}
peoples_lists = [peoples1,peoples2,peoples3]

for peoples_list in peoples_lists:
    for name_surname,name_city in peoples_list.items():
        print('\n' +name_surname +': ')
        print(name_city)

'''
需求6-8：
'''
pet1 = {
    'type' : 'cat',
    'pet_master' :'大马猴'
}

pet2 = {
    'type':'dog',
    'pet_master':'赵二狗'
}

pet3 = {
    'type':'cow',
    'pet_master':'王麻子'
}
pets = [pet1,pet2,pet3]
for pet in pets:
    for pet_key,pet_value in pet.items():
        print("\n"+pet_key+": ")
        print(pet_value)

'''
需求6-9
'''
favorite_places = {
    'jen':['China','Italy'],
    'sarah':['Russia'],
    'puil':['Thailand','Singapore']
}
for favorite_name,place_countries in favorite_places.items():
#上面for循环，是获取favorite_places字典中的人名和对应的国家
    print('\n' + favorite_name +'喜欢的国家是：')
    for place_countrie in place_countries:
    #上面for循环是循环获取每个国家
        print(place_countrie)

'''
需求6-10
'''
peoples_dicts = {"王大":[2,5,10],
                 "赵二":[3,6,9],
                 "张三":[2,4,6],
                 "李四":[1,3,9],
                 "王五":[9,10,11]
                 }
for people,dict in peoples_dicts.items():
    print('\n' + people + "喜欢的数字有：")
    print(dict)

'''
需求6-11：创建一个cities的字典，将三个城市用作键，对于每座城市，都创建一个字典，
包含country、population和fact等键，将其信息打印
'''

cities = {
    'bordeux':{
        'country':'france',
        'population':'243636',
        'fact':'水镜广场比特沙丘'},
    'larochelle' : {
        'country':'france',
        'population':'100000',
        'fact':'港口水族馆海贼梦世界尽头的灯塔'},
    'barcelona' : {
        'country':'spain',
        'population':'161000',
        'fact':'建筑教堂佛朗明哥'}
}
for city,info in cities.items():
    print('\n' + city + '介绍：')
    for cities_key,cities_value in info.items():
        print(cities_key + ': ' + cities_value)

