#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/23 10:14

'''
需求9-1：创建Restaurant的类，设置两个属性，restaurant_name和cuisine_type.
创建describe_restaurant()的方法和一个名为open_restaurant()的方法
'''

class Restaurant():
    """创建餐馆类"""
    def __init__(self,restaurant_name,cuisine_type):
        """类中的构造方法"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述方法的作用"""
        print('餐厅名称：' + self.restaurant_name +', 餐厅使用的冰箱类型是：' + self.cuisine_type)

    def open_restaurant(self):
        """打印餐厅正在营业中"""
        print('餐厅：' + self.restaurant_name +'正在营业')

#将类Restaurant的属性赋值给my_restaurant_01
my_restaurant_01 = Restaurant('元古川菜馆','海尔超大冰柜')
#调用类Restaurant下的describe_restaurant()和open_restaurant()方法
my_restaurant_01.describe_restaurant()
my_restaurant_01.open_restaurant()
#调用类Restaurant下的restaurant_name参数
print(my_restaurant_01.restaurant_name)

#二次调用类Restaurant中的describe_restaurant()方法
my_restaurant_02 = Restaurant('拿渡麻辣香锅','自制冷库')
my_restaurant_02.describe_restaurant()

#三次调用类Restaurant中的describe_restaurant()方法
my_restaurant_03 = Restaurant('旧县羊蝎子','没有冰柜')
my_restaurant_03.describe_restaurant()

class User():
    """创建一个用户类"""

    def __init__(self,first_name,last_name,age,city):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def desciribe_user(self):
        """打印用户信息"""
        print(
            '\n姓名：'+self.first_name+self.last_name+
            ', 年龄：'+ self.age +
            ', 所在城市:' + self.city
              )

    def greet_user(self):
        """打印问候语"""
        print('尊敬的：'+self.first_name+self.last_name+'先生/女士：早晨好！')

my_user = User('张','三','30','北京')
my_user.desciribe_user()
my_user.greet_user()


'''
需求9-4：在9-1中添加一个名为：number_served的属性，将其默认值等于0.
'''
class Restaurant():
    """创建餐馆类"""
    def __init__(self,restaurant_name,cuisine_type):
        """类中的构造方法"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        #设置就餐人数默认值为：0
        self.number_server = 0

    def set_number_severd(self):
        """打印就餐人数"""
        print('目前就餐人数为：' + str(self.number_server))

    def increment_number_severd(self,number):
        """将就餐人数递增"""
        self.number_server += number
        print('目前就餐人数为：' + str(self.number_server))

my_restaurant_04 = Restaurant('拿渡麻辣香锅','自制冷库')
#修改就餐人数为：6
my_restaurant_04.number_server = 6
my_restaurant_04.set_number_severd()
#递增就餐人员2人
my_restaurant_04.increment_number_severd(2)

'''
需求9-5：
'''
class User():
    """创建一个用户类"""

    def __init__(self,first_name,last_name,age,city,login_attempts):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = login_attempts

    def increment_login_attempts(self,attempts):
        """将login_attempts值+1"""
        self.login_attempts += attempts
        print('\nlogin_attempts值为：'+str(self.login_attempts))

    def reset_login_attemps(self):
        """将login_attempts重置为：0"""
        self.login_attempts = 0
        print("\nlogin_attempts值重置为："+str(self.login_attempts) )

my_user = User('张','三','30','北京',0)
my_user.increment_login_attempts(1)
my_user.increment_login_attempts(1)
my_user.increment_login_attempts(1)
my_user.increment_login_attempts(1)
my_user.reset_login_attemps()

'''
9-6需求：继承Restaurant类，编写一个IceCreamStand()的类，添加一个名为flavors的属性，
储存一个由各种口味的冰激凌组成的列表，创建一个IceCreamStand实列，并调用
'''

class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        '''继承Restaurant的构造方法，使用super()'''
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['vanilla','chocolate','durian']

    def print_flavors(self):
        '''打印self.flavors列表种的值'''
        print('\n')
        for flavor in self.flavors:
            print(flavor)

#创建IceCreamStand实例
my_restaurant_05 =  IceCreamStand('麦当劳甜品站','冰激凌')
#调用方法
my_restaurant_05.print_flavors()

'''
需求9-7：继承User,创建Admin的类，添加一个privileges的属性，存储如：
('can add post','can delete post','can ban user')等组成的列表
编写一个show_privileges()的方法，显示管理权限，创建Admin实例，并调用
'''
class Admin(User):

    def __init__(self,first_name,last_name,age,city):
        super().__init__(self,first_name,last_name,age,city)
        #self.privileges = ['can add post','can delete post','can ban user']
        self.privileges = '所有权限'

    def show_privileges(self):
        print('\n需求9-7：\n管理员的权限为：'+self.privileges)

my_user_01 = Admin('张','三','30','北京')
my_user_01.show_privileges()

'''
需求9-8：编写一个privileges的类，只有一个属性privileges,其中存储9-7所说的字符串，
将show_privileges移到这个类中，在Admin类中，将一个privileges的实例作为属性，
创建一个Admin实例，并使用show_privileges()来显示权限
'''
class Admin(User):

    def __init__(self,first_name,last_name,age,city):
        super().__init__(self,first_name,last_name,age,city)
        #self.privileges = '所有权限'

    def show_privileges(self):
        Privileges()

class Privileges():
        privileges = ['can add post','can delete post','can ban user']
        for privilege in privileges:
            print('\n需求9-8：'+privilege)

my_user_02 = Admin('张','三','30','北京')
my_user_02.show_privileges()

'''
需求9-9：
'''
class Car():

    def __init__(self,make,model,year):
        '''Car类初始化属性'''
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + '' + self.make + ''+self.model
        return long_name.title()

class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = '\n需求9-9：This car can go approximately ' + str(range)
        message += ' miles on a full chage.'
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

my_car = ElectricCar('tesla','model',2018)
my_car.upgrade_battery()
my_car.get_range()


