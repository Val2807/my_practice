#таблица умножения
for i in range(1,11):
   for j in range(1,11):
      print(i, "*", j, "=", i * j)
   print()


#чётные числа от 2 до 20
for i in range(0,21,2):
   print(i)
print()

#квадраты чисел от 1 до 10
for i in range (1,11):
   print(i, "*", i, "=", i * i)
print()


#сумма чисел от 1 до 100
total = 0
for i in range (1,101):
   total+=i
print(total)

#индексы
word = "programming"
print(word[0], word[-1], word[:4], word[::2], word[::-1])

lang = "programing"
print(len(lang))
print(lang[3:-3], lang[6:10], lang[0:5], lang[5:10], lang[1::2])
print()


string = "Python is fun!"
print(string[0:6])
print(string.replace(" ", ""))