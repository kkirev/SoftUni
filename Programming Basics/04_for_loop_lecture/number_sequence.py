#Напишете програма, която чете n на брой цели числа. Принтирайте най-голямото и най-малкото число сред въведените.

import sys

numbers_count = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for numbers in range(numbers_count):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')

# numbers_count = int(input())
# current_number = int(input())
# max_number = current_number
# min_number = current_number
#
# for numbers in range(numbers_count-1):
#     current_number = int(input())
#     if current_number > max_number:
#         max_number = current_number
#     if current_number < min_number:
#         min_number = current_number
# print(f'Max number: {max_number}')
# print(f'Min number: {min_number}')