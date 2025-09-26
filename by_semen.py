# #quadratic_equation
import math

# try:
#    a = float(input("Введите число a: "))
#    b = float(input("Введите число b: "))
#    c = float(input("Введите число c: "))

#    if a == 0:
#       print("Это не квадратное уравнение (a = 0)")
#    else:
#       D = b**2 - 4*a*c

#       if D > 0: 
#             sqrt_D = math.sqrt(D)
#             x1 = (-b + sqrt_D) / (2*a)
#             x2 = (-b - sqrt_D) / (2*a)
#             print(f"Два корня: {x1:.1f} и {x2:.1f}")
#       elif D == 0:
#             x = -b / (2*a)
#             print(f"Один корень: {x:.1f}") 
#       else:
#             print("Корней нет (дискриминант меньше 0)")

# except:
#       print("Ошибка: введите число")


hw/2025-09-16-function_quadratic_equation
def quadratic_equation (*, a: float, b: float, c: float) -> str:
      try:
            if a == 0:
                  answer = "Это не квадратное уравнение (a = 0)"
            
            else:
                  D = b**2 - 4*a*c
                  if D > 0: 
                        sqrt_D = math.sqrt(D)
                        x1 = (-b + sqrt_D) / (2*a)
                        x2 = (-b - sqrt_D) / (2*a)
                        answer = f"Два корня: {x1:.1f} и {x2:.1f}"
                  elif D == 0:
                        x = -b / (2*a)
                        answer = f"Один корень: {x:.1f}"
                  else:
                        answer = "Корней нет (дискриминант меньше 0)"
            return answer 
      except Exception as e:
            return f"Ошибка: {e}"

print(quadratic_equation(a=8, b=69, c=-21))


#a
z = 12
y = math.log(z / 4, 6)
print(y)

#b
z = math.sin(math.radians(17))
print(z)

#c
x = 3
z = 3 ** (x+2)
print(z)

#d 
y = (math.e ** 3) - 10 ** (-1.4)
print(y)

