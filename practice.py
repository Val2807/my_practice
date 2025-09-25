###задания с сайта https://python-academy.org/ru/trainer
# #1 product of numbers
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
# n = int(input())
# scores = list(map(int, input().split()))
# uniq_scores = set(scores)
# uniq_scores.remove(max(uniq_scores))
# print(max(uniq_scores))

# def second_max(numbers: list[int]) -> int:
#     uniq = set(numbers)
#     uniq.remove(max(uniq))
#     return max(uniq)

# print(second_max([1, 345, 542, 24, 543, 23]))

# #4
# n = int(input())
# students = {}
# for _ in range(n):
#     line = input().split()
#     name = line[0]  
#     marks = list(map(float, line[1:]))
#     students[name] = marks
    
# student_name = input()

# marks = students[student_name]

# avg = sum(marks) / len(marks)

# print(f"{avg:.2f}")

#5 

#6
# s = input()
#6.1
# new_symbols = []
# for symbol in s:
#     if symbol.isupper():
#         new_symbols.append(symbol.lower())
#     elif symbol.islower():
#         new_symbols.append(symbol.upper())
#     else:
#         new_symbols.append(symbol)

# print(''.join(new_symbols))

#6.2
# print(s.swapcase())

#8
s = input()
width = int(input())

def cut_string(string: str, width_num: int) -> str:
    parts = []
    for i in range(0, len(string), width_num):
        parts.append(string[i:i+width_num])
    return "\n".join(parts)

print(cut_string(s, width))







###задания с сайта https://pydocs.ru/prakticheskie-zadachi-po-bloku-vvedenie/#kvadrat
#основы. 1.площадь треугольника
# a = float(input('1 сторона: '))
# b = float(input('2 сторона: '))
# c = float(input('3 сторона: '))
# s = (a + b + c) / 2

# area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# print(area)

# import math

# def triangle_area(*, a: float, b: float, c: float) -> float:
#     p = (a + b + c) / 2
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     return s 

# print(triangle_area(a=3, b=4, c=5))

#основы. 2.перевод км в мили
# km = float(input("Enter value in km: "))

# #0,62 км в одной миле
# conv_fac = 0.612371

# miles = km * conv_fac
# print(km, 'километров в милях равна: ', miles)

#циклы. 1.чётность числа
# num = float(input("Enter your number: "))
# if num % 2 == 0:
#     print(f"{num} чётное число")
# else:
#     print(f"{num} нечётное число")



#циклы. 2.високосность года

# year = int(input("Enter the year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(year, "год високосный")
#         else:
#             print(year, "год не високосный")
#     else:
#         print(year, "год високосный")
# else:
#     print(year, "год не високосный")
       

# #циклы. 3.наибольшее из трёх
# num1 = 234
# num2 = 3355
# num3 = 24

# if num1 > num2 and num1 > num3:
#     biggest = num1
# elif num2 > num3 and num2 > num1:
#     biggest = num2
# else:
#     biggest = num3

# print("Наибольшее число из трёх чисел", biggest)

#циклы. 4.простые числа в интервале
# num_1 = int(input("Enter the lower number: "))
# num_2 = int(input("Enter the upper number: "))

# print("Диапазон чисел между", num_1, "и", num_2)

# for num in range(num_1, num_2 + 1):
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

# #циклы. 5.факториал числа 
# num = int(input("Enter the number: "))

# factorial = 1 

# if num < 0:
#     print("Для отрицательных чисел факториал не определен")

# elif num == 0:
#     print("Факториал 0 равен 1")

# else:
#     for i in range(1, num + 1):
#         factorial *= i

# print(f"Факториал {num} равен {factorial}") 
