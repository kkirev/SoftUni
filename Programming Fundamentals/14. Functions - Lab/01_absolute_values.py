"""
Write a program that receives a sequence of numbers, separated by a single space,
and prints their absolute value as a list. Use abs().
"""

numbers = input().split()
numbers_as_floats = []

for number in numbers:
	numbers_as_floats.append(abs(float(number)))

print(numbers_as_floats)

# print([abs(float(number)) for number in input().split()])