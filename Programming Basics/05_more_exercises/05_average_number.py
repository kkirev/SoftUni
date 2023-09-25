"""
https://judge.softuni.org/Contests/Practice/Index/1684#0

Напишете програма, която прочита едно число n, след това прочита n на брой цели числа и принтира средно аритметичното
на тяхната сума число, форматирано до втората цифра след десетични знак.
"""

numbers_count = int(input())

sum_numbers = 0

for i in range(numbers_count):
    number = int(input())
    sum_numbers += number

print(f'{sum_numbers / numbers_count:.2f}')