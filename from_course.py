#lists
numbers=[1,2,3,4,5]
print(numbers)
print()


#multiplication table
for i in range(1,11):
   for j in range(1,11):
      print(i, "*", j, "=", i * j)
   print()


#чётные числа от 2 до 20
for i in range(0,21,2):
   print(i)
print()

#qudratic from 1 to 10
for i in range (1,11):
   print(i, "*", i, "=", i * i)
print()


#sum from 1 to 100
total = 0
for i in range (1,101):
   total+=i
print(total)

#indexes
#упр1
word = "programming"
print(word[0], word[-1], word[:4], word[::2], word[::-1])

#exercise2
lang = "programing"
print(len(lang))
print(lang[3:-3], lang[6:10], lang[0:5], lang[5:10], lang[1::2])
print()

#exercise3
string = "Python is fun!"
print(string[0:6])
print(string.replace(" ", ""))
print()

#for
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
   if num % 2 == 0:
      continue
   print (num)
   print()

#functions
#exercise1_greeting
def greeting(name: str, greeting: str = "Hello") -> str:
   return f"{greeting}, {name}"


print(greeting(name="John"))

#exercise2_greting + input
def greeting(name: str, greeting: str = "Hello") -> str:
   return f"{greeting}, {name}"

user_name=input("Write your name: ")
print(greeting(user_name))





