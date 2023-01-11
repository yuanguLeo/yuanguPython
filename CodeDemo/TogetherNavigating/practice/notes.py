def display_message(study):
	"""显示简单的问候语"""
	print("第八章学习的是：" + study+'!')

display_message('函数')


def favorite_book(title):
	"""打印一条消息"""
	print("One of my favorite books is Alice in" + title.title() + ".")

favorite_book("wonderland")

# def describe_pet(anima_type,pet_name):
# 	"""显示宠物的信息"""
# 	print("I hava a " + anima_type + ".")
# 	print("My " + anima_type + "'s name is " + pet_name.title() + ".\n")

# describe_pet('hamster','harry')


def make_shirt(size,word = 'I love Python'):
	"""给T-shirt设计字样"""
	print("我的尺寸是：" +size +", 我要设计的字样是："+ word +".")

make_shirt('xxl')
make_shirt(word = 'Adhere to the', size = 'xl')

def describe_city(city,countries = '中国'):
	"""描述一座城市以及该城市所属的国家"""
	print(city + ' 在 ' + countries)

describe_city('北京')
describe_city('上海')


#返回值
# def get_formatted_name(first_name,last_name):
# 	"""返回整洁的姓名"""
# 	full_name = first_name + ' ' + last_name
# 	return full_name.title()

# musician = get_formatted_name('jimi','hendrix')
# print(musician)

def get_formatted_name(first_name,last_name,middle_name = ' '):
	"""让实参变成可选的"""
	full_name = first_name + middle_name + last_name
	return full_name.title()

musician1 = get_formatted_name('jimi','hendrix')
print(musician1)

musician2 = get_formatted_name('jimi ','hendrix','lee ')
print(musician2)


def city_country(city,countries):
	"""按照格式返回字符串"""
	country = city + ', ' + countries
	return country.title()

value = city_country('beijing','china')
print(value)


def make_album(album_name,singer_name,sing_number = 10):
	"""返回字典"""
	album = {"专辑名":album_name,"歌手名":singer_name,"歌曲数量":sing_number}
	return album

# value1 = make_album("此时此刻","许巍")
# value2 = make_album("无尽光芒","许巍")
# value3 = make_album("Jay","周杰伦",12)
# print(value1)
# print(value2)
# print(value3)


# while True:

# 	album_name = input("请输入专辑名称：")
# 	if album_name == 'q':
# 		break
	
# 	singer_name = input("请输入专辑的歌手：")
# 	if singer_name == 'q':
# 		break
		
	
# value = make_album(album_name,singer_name)
# print(value)

# def get_formatted_name(first_name, last_name):
# 	"""返回整洁的姓名"""
# 	full_name = first_name + ' ' + last_name
# 	return full_name.title()

# while True:
# 	print("\nPlease tell me your name:")
# 	print("(enter 'q' at any time to quit)")
	
# 	f_name = input("First name: ")
# 	if f_name == 'q':
# 		break

# 	l_name = input("Last name: ")
# 	if l_name == 'q':
# 		break

# formatted_name = get_formatted_name(f_name, l_name)
# print("\nHello, " + formatted_name + "!")


def greet_users(names):
	"""向列表中的每位用户都发出简单的问候"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)


# # 首先创建一个列表，其中包含一些要打印的设计
# old_names = ['iphone,'robot pendant','dodecahedron']
# new_names = []

# # 模拟打印每个设计，直到没有未打印的设计为止
# # 打印每个设计后，都将其移到列表new_names中
# while  old_names:
# 	design = old_names.pop()

# 	#模拟根据设计制作3D打印模型的过程
# 	print("Printing model: " + design)
# 	new_names.append(design)

# # 显示打印好的所有模型
# print("\nThe following models hava been printed: ")
# for new_name in new_names:
# 	print(new_name)

def print_models(old_names,new_names):
	while old_names:
		design = old_names.pop()

		print(design)
		new_names.append(design)


def show_names(new_names):
	print("\nThe following models hava been printed: ")
	for new_name in new_names:
		print(new_name)

old_names = ['iphone','robot pendant','dodecahedron']
new_names = []

print_models(old_names[:],new_names)
show_names(new_names)
print(old_names)

def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(old_magicians,new_magicians):
	while  old_magicians:
		design = old_magicians.pop()

		new_magicians.append("the Great "+ design)
		#print(new_magicians)

old_magicians = ['刘  谦','傅琰东','王亦丰']
new_magicians = []
make_great(old_magicians[:],new_magicians)
show_magicians(old_magicians)
show_magicians(new_magicians)


def make_pizza(*toppings):
	"""打印顾客点的所有配料"""
	print("\nMakeing a pizza with the following toppings:")
	for topping in toppings:
		print("-" + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green pepers','extra cheese')


def make_pizzas(size,*toppings):
	"""概述要制作的披萨"""
	print("\nMakeing a " + str(size) +
		"-inch pizza with the following toppings :")

	for  topping in toppings:
		print("- " + topping)

make_pizzas(16,'pepperoni')
make_pizzas(20,'mushrooms','green pepers','extra cheese')


# def build_profile(First,Last,**user_info):
# 	"""创建一个字典，其中包含我们知道的有关用户的一切"""
# 	profile = {}
# 	profile['first_name'] = First
# 	profile['Last_name'] = Last
# 	for key,value in user_info.items():
# 		profile[key] = value
# 	return profile

# user_profile = build_profile(
# 	'albert', 'einstein',
# 	location ='princeton',
# 	field ='physics')
# print(user_profile)



def make_sandwich(taste,*toppings):
	
	print("\n" + taste+"口味的三明治: " ) 
	for topping in toppings:
		print(topping)

make_sandwich("黑椒","不要辣")
make_sandwich("麻辣","夹肉","加菜","多麻多辣")


def build_profile(First,Last,**toppings):

	profile = {}
	profile['first_name'] = First
	profile['Last_name'] = Last

	for  key,value in toppings.items():
		profile[key] = value

	return profile

user_profile = build_profile('元','古',gender='男',address='北京')
print(user_profile)



def make_car(manufacturers,model,**other):
	car_dict = {}
	car_dict['manufacturers'] = manufacturers
	car_dict['model'] = model


	for key,value in other.items():
		car_dict[key] = value

	return car_dict

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


import pizza

pizza.make_pizza(16,'pepperoni')
make_pizzas(20,'mushrooms','green pepers','extra cheese')