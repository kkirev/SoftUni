"""
https://judge.softuni.org/Contests/2418

Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,
и проверява дали сред тях съществува число, което е равно на сумата на всички останали.
Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между
най-големия елемент и сумата на останалите (по абсолютна стойност)
"""

import sys

numbers_count = int(input())

numbers_sum = 0
max_num = -sys.maxsize

for numbers in range(numbers_count):
    current_num = int(input())
    numbers_sum += current_num
    if current_num > max_num:
        max_num = current_num

numbers_sum -= max_num
if max_num == numbers_sum:
    print('Yes')
    print(f'Sum = {numbers_sum}')
else:
    print('No')
    print(f'Diff = {abs(max_num - numbers_sum)}')