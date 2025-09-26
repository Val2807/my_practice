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

year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "год високосный")
        else:
            print(year, "год не високосный")
    else:
        print(year, "год високосный")
else:
    print(year, "год не високосный")
       

#циклы. 3.наибольшее из трёх
num1 = 234
num2 = 3355
num3 = 24

if num1 > num2 and num1 > num3:
    biggest = num1
elif num2 > num3 and num2 > num1:
    biggest = num2
else:
    biggest = num3

print("Наибольшее число из трёх чисел", biggest)

 