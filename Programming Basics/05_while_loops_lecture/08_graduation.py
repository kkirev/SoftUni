"""
https://judge.softuni.org/Contests/2419

Напишете програма, която изчислява средната оценка на ученик от цялото му обучение.
На първия ред ще получите името на ученика, а на всеки следващ ред неговите годишни оценки.
Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00.
Ако ученикът бъде скъсан повече от един път, то той бива изключен и програмата приключва,
като се отпечатва името на ученика и в кой клас бива изключен.
 При успешно завършване на 12-ти клас да се отпечата :
"{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
В случай, че ученикът е изключен от училище, да се отпечата:
"{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
Стойността трябва да бъде форматирана до втория знак след десетичната запетая.
"""

student_name = input()

current_class = 1
sum_grade = 0
fails = 0
is_excluded = False

while current_class <= 12:
    annual_grade = float(input())
    if annual_grade < 4:
        fails += 1
        if fails > 1:
            is_excluded = True
            break
    else:
        current_class += 1
        sum_grade += annual_grade
if is_excluded:
    print(f'{student_name} has been excluded at {current_class} grade')
else:
    average_rate = sum_grade / 12
    print(f'{student_name} graduated. Average grade: {average_rate:.2f}')

# -----------------------------------------------------------------------------
#
# student_name = input()
#
# current_class = 1
# sum_grade = 0
# fails = 0
#
# while True:
#     annual_grade = float(input())
#     if annual_grade < 4:
#         fails += 1
#         if fails >= 2:
#             print(f'{student_name} has been excluded at {current_class} grade')
#             break
#         continue
#     current_class += 1
#     sum_grade += annual_grade
#     if current_class > 12:
#         average_rate = sum_grade / 12
#         print(f'{student_name} graduated. Average grade: {average_rate:.2f}')
#         break