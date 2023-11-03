"""
Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
The input holds two lines: the number of people N and the capacity P of the elevator.
"""
# from math import ceil
#
# people_number = int(input())
# capacity = int(input())
#
# courses_count = people_number / capacity
# print(f'{ceil(courses_count)}')
# ---------------------------------------------------------------------------------------------------------------------
#
people_number = int(input())
capacity = int(input())

courses_count = people_number // capacity
if people_number % capacity != 0:
    courses_count += 1
print(courses_count)