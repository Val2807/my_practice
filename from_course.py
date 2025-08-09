#lists
# numbers=[1,2,3,4,5]
# print(numbers)
# print()


# #multiplication table
# for i in range(1,11):
#    for j in range(1,11):
#       print(i, "*", j, "=", i * j)
#    print()


# #чётные числа от 2 до 20
# for i in range(0,21,2):
#    print(i)
# print()

# #qudratic from 1 to 10
# for i in range (1,11):
#    print(i, "*", i, "=", i * i)
# print()


# #sum from 1 to 100
# total = 0
# for i in range (1,101):
#    total+=i
# print(total)

# #indexes
# #упр1
# word = "programming"
# print(word[0], word[-1], word[:4], word[::2], word[::-1])

# #exercise2
# lang = "programing"
# print(len(lang))
# print(lang[3:-3], lang[6:10], lang[0:5], lang[5:10], lang[1::2])
# print()

# #exercise3
# string = "Python is fun!"
# print(string[0:6])
# print(string.replace(" ", ""))
# print()

# #for
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#    if num % 2 == 0:
#       continue
#    print (num)
#    print()

# #functions
# #exercise1_greeting
# def greeting(name: str, greeting: str = "Hello") -> str:
#    return f"{greeting}, {name}"


# print(greeting(name="John"))

# #exercise2_greting + input
# def greeting(name: str, greeting: str = "Hello") -> str:
#    return f"{greeting}, {name}"

# user_name=input("Write your name: ")
# print(greeting(user_name))
# print()

# #exercise3_greeting input + for
# count = int(input("Сколько человек ты хочешь поприветсвовать? "))
# for i in range(count):
#    name=input("Please write your name ")
#    print(f"Good morning, {name}")

#exercise3.2_greeting input + for +list 
# count = int(input("Сколько человек ты хочешь поприветсвовать? "))
# names=[]
# for i in range(count):
#    name=input("Please write your name ")
#    names.append(name)
# for name in names:
#    print(f"Hello, {name}")
# count_letters=0

# for j in range(len(names)):
#    count_letters+=len(names[j])
# print(count_letters)  #мой вариант 

# for name in names:
#    count_letters += len(name)
# print(count_letters) #норм вариант

#exercise4_function(sum of numbers)

#сделал сам
# def add_numbers(*, number_1: float, number_2: float) -> float:
#    numbers_sum=number_1+number_2
#    return f"Сумма чисел {number_1} и {number_2} равна {numbers_sum}"
# print(add_numbers(number_1=3, number_2=4))

# #с чатом оптимизировал
# def add_numbers(*, number_1: float, number_2: float) -> float:
#    return number_1+number_2
# result = add_numbers(number_1=3, number_2=4)
# print(f"Сумма чисел равна {result}") 


#отработка
# #1
# def add_numbers(a: float, b: float) -> float:
#    return a+b
# print(add_numbers(4, 5))


# def multiply_or_add (a: float, b: float, operation: str):
#    if operation == "multiply":
#       return a*b
#    elif operation == "aad":
#       return a+b
#    else:
#       return "Unknown operation" 
# result = multiply_or_add(a=3, b=4, operation="multiply")
# print(result)


# def three_option (a: float, b: float, c: float, operation: str):
#    if operation == "sum":
#       return a+b+c
#    elif operation == "avg":
#       return (a+b+c)/3
#    elif operation == "max":
#       return max(a, b, c)
#    else:
#       return "Unknown operation"
# result = three_option(a=5, b=3, c=10, operation="avg")
# print(result)

# #2
# def area_of_rectangle(length: float, width: float) -> float:
#    return length*width
# print(area_of_rectangle(length=2, width=7))

# #3
# def even_number(a: int) -> int:
#    if a % 2 == 0:
#       return f"{a} - чётное число"
#    else:
#       return f"{a} - не чётное число"

# print(even_number(a=2))

# #3.1 (вместе с input)
# def even_number(a: int) -> int:
#    if a % 2 == 0:
#       return f"{a} - чётное число"
#    else:
#       return f"{a} - не чётное число"

# while True:
# 	try:
# 		number = int(input("Введите число "))
# 		print(even_number(number))
# 		break
# 	except ValueError:
# 		print("Error: write the number")


#3

# def introduсe(*, name: str, age: int) -> str:
#    if age is None:
#       age = 18
#    return f"Привет, меня зовут {name}, мой возраст {age} лет"
# print(introduсe(name="Valentin", age=None))

# def introduсe(*, name: str, age: int=18):
#    return f"Привет, меня зовут {name}, мой возраст {age} лет"
# print(introduсe(name="Valentin"))


# #3.1

# def order_summary(*, item: str, quantity: int=1, price: int=100) -> str:
#    total = quantity * price
#    return f"Вы заказали {quantity} x {item} на сумму {total} рублей" 
# print(order_summary(item="stick", quantity=3))

#4
# def age_category(age: int) -> str:
#    if age < 12:
#       return "ребёнок"
#    elif 12 <= age <= 17:
#       return "подросток"
#    else:
#       return "взрослый"
# print(age_category(age=45))

# #5
# def max_of_three(a: int, b: int, c: int) -> int:
#    if a > b and a > c:
#       return a
#    elif b > a and b > c:
#       return b
#    elif c > a and c > b:
#       return c
#    else:
#       return f"numbers are same"
# print(max_of_three(a=10, b=10, c=10))

# #5.1 встроенная функция "max"
# def max_of_three(a: int, b: int, c: int) -> int:
#     return max(a, b, c)

# print(max_of_three(4, 10, 6))

#6
def string_length(text: str) -> int:
   return len(text)
print(string_length(text="Hello"))

#7
def remove_spaces(text: str) -> str:
   return text.strip()
print(remove_spaces("     Hello, world     "))

#8
def remove_all_spaces(text: str) -> str:
   remove_outside_spaces = text.strip()
   remove_inside_spaces = text.replace(" ", "")
   return remove_outside_spaces and remove_inside_spaces
print(remove_all_spaces(text="     Hello,    world       "))

#8.1 (чат)
def remove_all_spaces(text: str) -> str:
   no_outside_spaces = text.strip()
   words = no_outside_spaces.split()
   cleaned_text = " ".join(words)
   return cleaned_text

print(remove_all_spaces("     Hello,    world       "))

#научился открывать ветку
print("Hello, world")