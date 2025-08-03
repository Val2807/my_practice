#quadratic_equation
import math

try:
   a = float(input("Введите число a: "))
   b = float(input("Введите число b: "))
   c = float(input("Введите число c: "))

   if a == 0:
      print("Это не квадратное уравнение (a = 0)")
   else:
      D = b**2 - 4*a*c

      if D > 0: 
            sqrt_D = math.sqrt(D)
            x1 = (-b + sqrt_D) / (2*a)
            x2 = (-b - sqrt_D) / (2*a)
            print(f"Два корня: {x1:.1f} и {x2:.1f}")
      elif D == 0:
            x = -b / (2*a)
            print(f"Один корень: {x:.1f}") 
      else:
            print("Корней нет (дискриминант меньше 0)")

except:
      print("Ошибка: введите число")