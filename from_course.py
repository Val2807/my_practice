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
def add_numbers(*, number_1: float, number_2: float) -> float:
   numbers_sum=number_1+number_2
   return f"Сумма чисел {number_1} и {number_2} равна {numbers_sum}"
print(add_numbers(number_1=3, number_2=4))

#с чатом оптимизировал
def add_numbers(*, number_1: float, number_2: float) -> float:
   return number_1+number_2
result = add_numbers(number_1=3, number_2=4)
print(f"Сумма чисел равна {result}") 


