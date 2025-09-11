# #1product of numbers
# numbers = list(map(int, input("Enter your numbers ").split()))

# total = 1
# for num in numbers:
# 	total *= num

# print(total)

# #2uniq_numbers
# numbers = list(map(int, input().split()))

# uniq_numbers = set(numbers)

# print(len(uniq_numbers)) 

#3 second maximum number from list






#распаковка
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