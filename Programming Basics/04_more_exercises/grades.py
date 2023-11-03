"""
https://judge.softuni.org/Contests/Practice/Index/1680#0

#Напишете програма, която да пресмята статистика на оценки от изпит. В началото програмата получава броят на
студентите явили се на изпита и за всеки студент неговата оценка. На края програмата трябва да изпечата процента на
студенти с оценка между 2.00 и 2.99, между 3.00 и 3.99, между 4.00 и 4.99, 5.00 или повече. Също така и
средният успех на изпита.
Вход
От конзолата се четат поредица от числа, всяко на отделен ред:
•	На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
•	За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
Изход
Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
Ред 1 -	"Top students: {процент студенти с успех 5.00 или повече}%"
Ред 2 -	"Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
Ред 3 -	"Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
Ред 4 -	"Fail: {по-малко от 3.00}%"
Ред 5 -	"Average: {среден успех}"
Всички числа трябва да са форматирани до вторият знак след десетичната запетая.
"""

# User input
students_count = int(input())

# Variables
students_5_to_6 = 0
students_4_to_5 = 0
students_3_to_4 = 0
students_failed = 0
total_grades = 0

# Logic
for student in range(students_count):
    exam_grade = float(input())
    if 5 <= exam_grade <= 6:
        students_5_to_6 += 1
        total_grades += exam_grade
    elif 4 <= exam_grade < 5:
        students_4_to_5 += 1
        total_grades += exam_grade
    elif 3 <= exam_grade < 4:
        students_3_to_4 += 1
        total_grades += exam_grade
    elif exam_grade < 3:
        students_failed += 1
        total_grades += exam_grade

average_grade = total_grades / students_count

# Output
print(f'Top students: {students_5_to_6 / students_count * 100:.2f}%')
print(f'Between 4.00 and 4.99: {students_4_to_5 / students_count * 100:.2f}%')
print(f'Between 3.00 and 3.99: {students_3_to_4 / students_count * 100:.2f}%')
print(f'Fail: {students_failed / students_count * 100:.2f}%')
print(f'Average: {average_grade:.2f}')