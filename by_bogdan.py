# def hello(name):
# 	return f"hello, {name}"

# print(hello("Vale"))

# #option 1
# def sum_nums(route, b):
# 	sum = route + b
# 	print(sum)


# sum_nums(10, 5)

# #option 2
# def sum_nums(route, b):
# 	sum = route + b
# 	return sum  #statement


# first_sum = sum_nums(10, 5)
# print(first_sum)

# #option 3
# def sum_nums(route, b):
# 	sum = route + b
# 	return sum

# print(sum_nums(route=10, b=5))

# print(sum_nums(sum_nums(10, 5), 30))

# def sum(route, b,):
# 	return route + b

# print(sum(3, 5))


# my_name = 'Vale'

# print(id(my_name))

# my_num = 100

# print(id(my_num))

# other_num = my_num
# print(id(other_num))


# db_is_available = False

# print(db_is_available)


# #магические методы
# float_num = 50.3
# str_val = 'abc'

# # print(str_val * float_num)

# # print(float_num.__mul__(str_val))

# # print(str_val.__rmul__(float_num))


# print(bool.__doc__)


# posts_ids = [23, 43, 3, 409]

# posts_ids.sort()

# print(posts_ids)

# posts_ids.sort(reverse=True)

# print(posts_ids)


# greeting = "Hello from Python"
# greeting_letters = list(greeting)

# print(greeting_letters)

# my_dict = {'route': 10, 'b': True}
# my_dict_keys = list(my_dict)

# print(my_dict_keys)


# my_nums = [10, 50, 0 , 5, 5, 100]

# other_nums = my_nums[:]

# my_nums.append(3)
# other_nums.clear()

# print(id(my_nums))
# print(id(other_nums))

# print(other_nums, my_nums)


# #homework
# #exersice1
# player_list = ['Sarp', 10, 20.5, True, [1]] #1

# player_list.pop(2)  #2

# #del player_list[2]  #2.1

# print(len(player_list))  #3

# player_list.reverse()  #4

# new_player_list = ['Duha', 'Atakan']  #5

# player_list.extend(new_player_list)  #6

# print(player_list)  #7

# exersice2

# my_list_1 = ['Anton', 'Max', 'Vita']
# my_list_2 = ['Vale', 'Son', 'Iana']   #1

# new_list = my_list_1 + my_list_2  #2
# print(new_list)

# #3

# new_list_2 = my_list_1.__add__(my_list_2)  #4
# print(new_list_2)


# my_motorbike = {
# 	'brand': 'Ducati',
# 	'price': 25000,
# 	'engine_vol': 1.2,
# }

# my_motorbike = {
# 	'brand': 'Honda',
# 	'price': 15000
# }

# my_motorbike['price'] = 20000

# print(my_motorbike['price'])

# my_motorbike = {
# 	'brand': 'Ducati',
# 	'Price': 25000,
# 	'engine_vol': 1.2,
# }

# key_name = 'brand'

# my_motorbike[key_name] = 'BMW'

# print(my_motorbike)

# print(my_motorbike.get('brand'))

# print(my_motorbike.get('model', 'unknown'))

# dict
# my_disk = {}

# print(id(my_disk))
# print(type(my_disk))


# my_disk['brand'] = 'Samsung'
# my_disk['price'] = '80'

# # print(my_disk)

# new_disk = my_disk.copy()

# new_disk['type'] = 'ssd'

# print(my_disk)
# print(new_disk)


# my_list = [['first', 0], ['second', True]]

# my_dict = dict(my_list)

# print(my_dict)

# homework_dicts

# practice_plan = {}

# dict_1_key = input("Please write name of key ")
# dict_1_value = input("Please write name of value ")
# practice_plan[dict_1_key] = dict_1_value


# dict_2_key = input("Please write name of key ")
# dict_2_value = input("Please write name of value ")
# practice_plan[dict_2_key] = dict_2_value


# dict_3_key = input("Please write name of key ")
# dict_3_value = input("Please write name of value ")
# practice_plan[dict_3_key] = dict_3_value


# print(practice_plan)

# practice_plan['day'] = 'Monday'
# practice_plan['kind'] = 'individual'

# print(practice_plan)

# del practice_plan[dict_2_key]
# del practice_plan[dict_1_key]


# print(practice_plan.get('kind'))

# print(practice_plan[dict_3_key])

# print(practice_plan)

# with for
# practice_plan = {}

# for i in range(3):
# 	dict_key = input("Please write name of key ")
# 	dict_value = input("Please write name of value ")
# 	practice_plan[dict_key] = dict_value

# print(practice_plan)

# tuples

# my_nums = (10, 5, 100, 0, 5, 5)

# index_1 = my_nums.index(5)
# index_2 = my_nums.index(5, index_1 + 1)
# index_3 = my_nums.index(5, index_2 + 1)
# print(index_3)

# my_list = list(my_nums)

# my_list.append(7)

# my_nums = tuple(my_list)


# print(my_nums)


# tuples
# my_tuple = (32, {'name': 'Vale', 'age': 23}, ['BMW', 'Mersedes', 'AUDI'])
# other_tuple = (10.5, 'abc')

# total_tuple = my_tuple + other_tuple

# print(total_tuple)

# set
# my_set = {2, 10}
# my_set.add(34)
# other_set = {56, 2, 46, 10, 34}
# general_set = my_set.intersection(other_set)
# general_set_list = list(general_set)

# print(general_set_list)

# print(my_set & other_set)

# print(my_set | other_set)

# print(my_set.issubset(other_set))

# range
# for n in range(2, 34, 4):
# 	print(n)

# print(list(range(12, 25, 5)))

# my_range = range(5, 20)
# print(my_range.index(13))

# #hw
# new_range = range (10, 30, 2)

# my_list = []
# for n in new_range:
# 	my_list.append(n)

# print(my_list)

# my_list_1 = [1, 2, 3]
# my_list_1.append(5)
# my_list_1.extend([6])
# print(my_list_1)


# set
# football = {"Иван", "Сергей", "Али", "Мехмет"}
# hockey   = {"Сергей", "Али", "Денис", "Ахмет"}

# f_h = football & hockey
# f = football - hockey
# f_or_h = football | hockey
# print(f_h, f, f_or_h)

# fruits = ['apple', 'banana', 'lime']

# quantities = 100, 70, 50

# availability = [True, False, False, True]

# fruit_qtys_zip = zip(fruits, quantities, availability)

# print(fruit_qtys_zip)

# fruit_qtys_zip = list(fruit_qtys_zip)

# print(fruit_qtys_zip)


# goods = ['cola', 'beer', 'bread']
# prices = [50, 98, 45]

# goods_prices_zip = zip(goods, prices)


# goods_prices_dict = dict(goods_prices_zip)

# print(goods_prices_dict)


# from copy import deepcopy

# info = {
# 	'name': 'Vale',
# 	'is_instruttor': True,
# 	'reviews': []
# }

# info_deepcopy = info.copy( )

# info_deepcopy['reviews'].append('great course')

# print(info)
# print(info_deepcopy)


# def sum(route, b):
# 	c = route + b
# 	return c

# sum(2, 6)
# sum(4, 5)

# def my_fn(route, b):
# 	route = route + 1
# 	c = route + b
# 	return c

# print(my_fn(10, 3))
# person_one = {
# 	'name': 'Bob',
# 	'age': 21
# }

# def increse_person_age(person):
# 	person_copy = person.copy()
# 	person_copy['age'] += 1
# 	return person_copy


# new_person = increse_person_age(person_one)
# print(person_one['age'])
# print(new_person['age'])

# def merge_list_to_dict(names, ages):
# 	list_zip = zip(names, ages)
# 	return dict(list_zip)

# print(merge_list_to_dict(names= ['Vale', 'Max', 'Anton'], ages= [23, 45, 13]))
# print(merge_list_to_dict(['Sarp', 'Duru', 'Aslan'], ages= [12, 12, 7]))

# def update_car_info(**car):
# 	car['is available'] = True
# 	return car
# print(update_car_info(model='BMW', year= 2015))
# print(update_car_info(model='BMW', year= 2015))

# from datetime import datetime
# def get_weekday():
# 	return datetime.now().strftime("%A")

# def create_new_post(post, weekday=get_weekday()):
# 	post_copy = post.copy()
# 	post_copy['created_on_weekday'] = weekday
# 	return post_copy


# initial_post = {
# 	'id': 243,
# 	'author': 'Vale'
# }

# post_with_weekday = create_new_post(initial_post)


# print(post_with_weekday)

# print(initial_post)


# def sum_nums(*args):
# 	print(args)
# 	print(type(args))

# 	print(args[0])
# 	return sum(args)

# print(sum_nums(2, 3, 7, 8))


# def get_posts_info(name, posts_qty):
# 	info = f"{name} wrote {posts_qty} posts"
# 	return info

# info = get_posts_info('Bogdan', posts_qty=25)
# print(info)

# def get_posts_info(**person):
# 	print(person)

# 	print(type(person))
# 	info = (
# 		f"{person['name'] } wrote "
# 		f"{person['posts_qty']} posts"
# 	)
# 	return info

# print(get_posts_info(name='Vale', posts_qty=25))


# def print_number_info(num):
# 	if (num % 2) == 0:
# 		print("Entered number is even")
# 	else:
# 		print("Entered number is odd")

# def print_square_num(num):
# 	print("Square of the num is", num * num)

# def process_number(num, callback_fn):
# 	callback_fn(num)

# entered_num = int(input('Enter any number: '))

# process_number(entered_num, print_number_info)
# process_number(entered_num, print_square_num)


# def print_number(num):
# 	"""_summary_

# 	Args:
# 		num (_type_): _description_
# 	"""

# 	print_number()

# def my_fn(route, b):
# 	print (route, b)

# my_fn('abc', 'xyz')


# first_set = {'apple', 'mango', 'banana'}
# secod_set = {'apple', 'mango', 'banana'}

# print(first_set == secod_set)
# print(first_set is secod_set)
# print('banana' in first_set)

# print(bool(0))
# print(bool(0.0))
# print(not not(0j))
# print(not not())

# my_list = [1, 2]

# print(my_list and "list is not empty")


# dict_one = {
# 	'player_1': "14 points",
# 	'player_2': "10 points",
# }

# dict_two = {
# 	'player_1': "14 points",
# 	'player_2': "10 points",
# }

# print(dict_one == dict_two and "dictionary are equal")

# оператор распаковки словаря **
# button_default = {
# 	'text': 'Okay',
# 	'color': 'black',
# 	'width': 0,
# 	'height': 0,
# }

# button_style = {
# 	'color': 'red',
# 	'width': 200,
# 	'height': 300
# }

# button_example = {
# 	'color': 'green',
# 	'size': 200*2,
# 	'shape': 'threeangle'
# }

# button = {
# 	**button_default,
# 	**button_example,
# 	**button_style,
# }

# print(button_default | button_style | button_example)
# print(button)

# my_name = 'Vale'
# my_hobby = 'running'
# time = 8

# info = my_name + ' likes ' + my_hobby + ' at ' + time + " o'clock"

# info = f"{my_name} likes {my_hobby} at {str(time)} clock"
# print(info.title())

# my_name = 'Vale'
# my_age = 25
# my_parents = ['Yurii', 'Galina']
# my_adres = {'city': 'Istanbul', 'street': 'sk 2288', 'building': '5'}

# info = f"{my_name} lives in {my_adres} with his parents {my_parents} and he's {my_age} years old"
# print(info)

# def mult(route, b):
# 	return route * b

# mult = lambda route, b: route * b

# print(mult(10, 5))


# #замыкание с ф-ией лямбда
# def greeting(greet):
# 	def info(name):
# 		return f"{greet}, {name}."
# 	return info


# morning_greeting = greeting("Good morning")

# print(morning_greeting('Vale'))

# evening_greeting = greeting("Good evening")

# print(evening_greeting('Bogdan'))

# general_greeting = greeting('Hello')

# print(general_greeting("dear guest"))

# try:
# 	print(10/0)
# except ZeroDivisionError as e:
# 	print(isinstance())
# 	print(e)

# except TypeError as e:
# 	print(e)


# print('Continue...')


# def image_info(img):
# 	if ('image_id' not in img) or ('image_title' not in img):
# 		raise TypeError("Keys image_id and image_title must be present")
# 	return f"Image {img['image_title']} has id {img['image_id']}"


# dict_image = {
# 	'image_id': 2345,
# 	'image_weight': '154mb',
# }


# try:
# 	print(image_info(dict_image))

# except TypeError as e:
# 	print(e)


# распаковка
# my_list = [1, 2, 3]

# first, second, third = my_list

# print(first)
# print(second)
# print(third)

# user_profile = {
# 	'name': 'Bogdan',
# 	'comments_qty': 23,
# }

# def user_info(name, comments_qty=0):
# 	if not comments_qty:
# 		return f"{name} has no comments"

# 	return f"{name} has {comments_qty} comments"

# print(user_info(**user_profile))


# list_dict = [{'brand': 'Bauer', 'remainder': 2},
# 				{'brand': 'ccm', 'remainder': 0},
# 				{'brand': 'sher wood', 'remainder': '5'}]

# first, second, third = list_dict

# def sticks_info(brand, remainder):
# 	if remainder == 0:
# 		return f"We don't have stciks in stock by {brand}"

# 	return f"We have {remainder} stciks in stock by {brand}"

# print(sticks_info(**first))
# print(sticks_info(**second))
# print(sticks_info(**third))

# def sticks_info_1():
# 	pass


# if, elif, else
# def nums_info(route, b):
# 	if (type(route) is not int) or (type(b) is not int):
# 		return f"Один из аргументов не целое число"

# 	if route>= b:
# 		return f"{route} больше или равно {b}"

# 	return f"{route} меньше {b}"

# print(nums_info(True, 10))
# print(nums_info(10, 2))
# print(nums_info(4, 15))

# def nums_info(route, b):
# 	if (type(route) is not int) or (type(b) is not int):
# 		info = "Один из аргументов не целое число"
# 	elif route>= b:
# 		info = f"{route} больше или равно {b}"
# 	else:
# 		info = f"{route} меньше {b}"
# 	return info

# print(nums_info(True, 10))
# print(nums_info(10, 2))
# print(nums_info(4, 15))


# def route_info(route):
# 	if "distance" in route and type(route['distance']) is int:
# 		distance_answer = f"Distance to your destination is {route['distance']}"
# 	elif "speed" in route and "time" in route:
# 		distance_answer = f"Distance to your destination is {route['speed'] * route['time']}"
# 	else:
# 		distance_answer = f"No distance info is available"
# 	return distance_answer

# route_info_dict = {
# 'speed': 50,
# }

# print(route_info(route_info_dict))

# my__img = ('1920', '1080')

# info = f"{my__img[0]}x{my__img[1]}" if len(my__img) == 2 else 'incorrect img'

# print(info)


# if len(my__img) == 2:
# 	print(f"{my__img[0]}x{my__img[1]}")
# else:
# 	print('incorrect img')


# my_str = "fkktokg otkokgokot moormormfm 5ogjrmvmq4ievmtmfvm mmormvo rvomomot  ormormmfoldoe oeld,kr,dkf"

# info = "string is long" if len(my_str) > 94 else "string is short"
# print(info)

# iterations
# my_object = {
# 	'x': 10,
# 	'y': True,
# 	'z': 'abc'
# }

# for key in my_object:
# 	print(my_object[key])

# for el in [1, 'abc', True]:
# 	print(type(el))
# 	print(el)

# my_dict = {'id': 324, 'title': 'test'}

# for key in my_dict:
# 	print(type(key))
# 	print(my_dict[key])

# #items()

# my_object = {
# 	'x': 10,
# 	'y': True
# }

# for item in my_object.items():
# 	key, value = item
# 	print(key, value)

# for k, v in my_object.items():
# 	print(k, v)


# #exersice_1
# my_dict = {
# 	'Bauer': 'Vapor',
# 	'CCM': 'SuperTacks',
# 	'price': 2000
# }


# def dict_to_list(dict_to_convert):
# 	list_to_convertion = []
# 	for key, value in dict_to_convert.items():
# 		if type(value) == int:
# 			value *= 2
# 		list_to_convertion.append((key, value))
# 	return list_to_convertion

# print(dict_to_list(my_dict))


# #exersice_1.2
# my_list = [122, True, 'car', 134, (21, 34, 'cat')]

# def filter_list(list_to_filter, value_type):
# 	filtered_list = []
# 	for value in list_to_filter:
# 			if type(value) == value_type:
# 				filtered_list.append(value)
# 	return filtered_list

# 1
# exercise
# while True:
# 	try:
# 		num_1 = float(input("Write the first number: "))
# 		num_2 = float(input("Write the second number: "))
# 	except ValueError as e:
# 		print(e)
# 		print("You must enter numbers!")
# 		continue

# 	print(num_2 / num_1)

# 	answer = input("Do you want to continiue? (yes/no): ")
# 	if answer == 'no':
# 		break

# list comprehensions (сокращенный цикл for in)
# not short for in
# all_nums = [-3, 1, 0, 10, -20, 5]

# absolute_nums = []

# for num in all_nums:
# 	absolute_nums.append(abs(num))

# print(absolute_nums)

# print(all_nums)

# #short for in
# all_nums = [-3, 1, 0, 10, -20, 5]

# absolute_nums = [abs(num) for num in all_nums]

# print(absolute_nums)

# print(all_nums)

# #forming a new list with filtration
# #long version
# all_nums = [-3, 1, 0, 10, -20, 5]

# positive_nums = []

# for num in all_nums:
# 	if num > 0:
# 		positive_nums.append(num)

# print(positive_nums)

# print(all_nums)

# #short version
# all_nums = [-3, 1, 0, 10, -20, 5]
# positive_nums = [num for num in all_nums if num > 0]

# print(positive_nums)

# print(all_nums)

# #set for in
# my_set = {1, 10, 15}

# new_set = set()

# for val in my_set:
# 	new_set.add(val * val)

# print(new_set)

# print(my_set)

# #short for in
# my_set = {1, 10, 15}
# new_set = {val * val for val in my_set}

# print(new_set)
# print(my_set)

# my_scores = {
# 	'a': 10,
# 	'b': 7,
# 	'm': 14
# }

# scores = {}

# for key, value in my_scores.items():
# 	scores[key] = value * 10

# print(scores)

# print(my_scores)

# #short
# my_scores = {
# 	'a': 10,
# 	'b': 7,
# 	'm': 14
# }

# scores = {v * 10 for k, v in my_scores.items()}

# print(scores)

# #from list to dict
# my_scores = [10, 7, 14]

# scores = {k: v for k, v in enumerate(my_scores)}

# print(scores)

# exercise_1
# dict_one = {
#     'name': 'valentin',
#     'surname': 'nikonorov',
# }

# new_dict = {k: v.upper() for k, v in dict_one.items()}

# print(new_dict)

# # exercise_1.2
# surname_list = ['Vale', 'Anton', 'Max']

# long_surname_list = [elem for elem in surname_list if len(elem) > 3]

# print(long_surname_list)


# classes and objects
# class Car:
#     def move(self):
#         print("Car is moving")

#     def stop(self):
#         print("Car stoped")


# my_car = Car()
# my_car.move()
# my_car.stop()

# print(my_car)
# print(type(my_car))
# print(isinstance(my_car, Car))
# print(isinstance(my_car, object))
# print(dir(my_car))

# my_second_car = Car()

# print(my_car == my_second_car)

# Car.move(my_car)


# Creating an instance of a class
class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self, qty):
        self.votes_qty += qty

    def reset_votes_qty(self):
        self.votes_qty = 0


my_comment = Comment("My coment")

print(my_comment.votes_qty)

my_comment.upvote(10)
my_comment.upvote(20)

print(my_comment.votes_qty)

my_comment.reset_votes_qty()

print(my_comment.votes_qty)


# exercise_classes_1

class Image:
    def __init__(self):
        self.resolution = '1920 x 1080'
        self.title = 'photo'
        self.extension = 'png'

    def resize(self, resolution):
        self.resolution = resolution

    def upper_title(self):
        self.title = self.title.upper()


new_image = Image()
print(new_image.resolution)
print(new_image.extension)

new_image.resize('1600 x 1200')
print(new_image.resolution)

new_image.upper_title()
print(new_image.title)
