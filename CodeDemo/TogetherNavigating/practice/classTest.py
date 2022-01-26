class Dog():
#	"""一次模拟小狗的简单尝试"""

	def __init__(self,name,age):
		"""初始化属性name和age"""
		self.name = name 
		self.age = age

	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + " roll over!")


my_dog = Dog('willie', 6)
print("My dog's name is "+ my_dog.name.title()+ ".")
print("My dog is " + str(my_dog.age) +" years old.")

my_dog.sit()
my_dog.roll_over()
print("___________________________________")

#9-1
class Restaurant():
	"""docstring for Restaurant"""
	def __init__(self,restaurant_name,restaurant_type):
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type

	def describe_restaurant(self):
		print(self.restaurant_name + "的招牌是" + self.restaurant_type + "。")

	def open_restaurant(self):
		print(self.restaurant_name + "餐厅正在营业中！")

	def increment_number_served(self,number_served):
		self.number_served += number_served

	def dining_number(self):
		print("该餐厅共有： " + str(self.number_served) + "人就餐！")


restaurant = Restaurant("全聚德","北京菜")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("___________________________________")

#9-2
restaurant01 = Restaurant("全聚德","烤鸭")
restaurant01.describe_restaurant()

restaurant02 = Restaurant("小肠陈","卤煮火烧")
restaurant02.describe_restaurant()

restaurant03 = Restaurant("东来顺","老北京火锅")
restaurant03.describe_restaurant()
print("___________________________________")

#9-4.1 
restaurant01.number_served = 20
restaurant01.dining_number()
print("___________________________________")

#9-4.2
restaurant01.increment_number_served(20)
restaurant01.dining_number()
print("___________________________________")

#9-3
class User():

	def __init__(self,fiset_name,last_name,age,):
		self.fiset_name = fiset_name
		self.last_name = last_name
		self.age = age
		self.login_attempts=0

	def describe_user(self):
		print("我叫：" + self.fiset_name + self.last_name +", 今年" + str(self.age) +"岁啦！")

	def greet_user(self):
		print("你好, " + self.fiset_name + self.last_name + ", 欢迎来到中国北京！")

	def increment_login_attempts(self):
		self.login_attempts += 1
		print(self.login_attempts)

	def reset_login_attempts(self):
		self.login_attempts = 0
		print(self.login_attempts)


user = User("张","大",23)
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
print("___________________________________")


class Car():
	
	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def update_odometer(self,mileage):
		"""将里程表读数设置为指定的值"""
		self.odometer_reading = mileage

	def increment_odometer(self,miles):
		"""将里程表读数增加指定的量"""
		self.odometer_reading += miles

	def fill_gas_tank(self):
		"""油箱的容积"""
		print("我的油箱可以装450升汽油！")
		
	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.increment_odometer(400)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_new_car.fill_gas_tank()
print("___________________________________")

#继承

class ElectricCar(Car):

	def __init__(self,make,model,year):
		""""初始化父类的属性"""
		super().__init__(make,model,year)
		self.battery_size = 70

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print("This car has a " + str(self.battery_size) + "-KWh battery.")

	def fill_gas_tank(self):
		"""电动车没有油箱"""
		print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
print("___________________________________")



