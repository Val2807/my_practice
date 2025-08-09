# задание
# Есть список словарей со студентами `students`. В каждом объекте есть имя и фамилия студента,
# а также список оценок (целых чисел). Нужно написать функцию get_best_students, которая берёт студентов и находит того,
# у кого средний балл наибольший. Возвращает функция список студентов с лучшим баллом. У некоторых студентов в оценках
# есть None: их среднюю оценку мы считаем равной 0.


students = [
    {"name": "John", "surname": "Doe", "grades": [5, 5, 4, 4]},
    {"name": "Jane", "surname": "Doe", "grades": [4, 3, 4, 3, 5]},
    {"name": "Bill", "surname": "Gates", "grades": [5, 5, 5, 3]},
    {"name": "Steve", "surname": "Jobs", "grades": [3, 5, 4, 3, 3, 5]},
    {"name": "Guido", "surname": "Van Rossum", "grades": [5, 3, 5, 4, 5, 5, 3, 5]},
    {"name": "Elon", "surname": "Musk", "grades": None}
]


#решение

averaged_students = []

for student in students:
   grades = student["grades"]
   name = student["name"]
   surname = student["surname"]
   
   if grades is None:
      average = 0
   else:
      average = round((sum(grades) / len(grades)), 2)
   student_avg = {"name": name, "surname": surname, "average": average}
   averaged_students.append(student_avg)

print(averaged_students)

the_best_student = max(averaged_students, key=lambda student: student["average"])
max_average = max(student["average"] for student in averaged_students)
best_students = [student for student in averaged_students if student["average"] == max_average]
print(best_students)




