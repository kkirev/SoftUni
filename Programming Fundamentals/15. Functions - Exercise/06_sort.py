"""
Write a program that receives a sequence of numbers (integers) separated by a single space.
It should print a sorted list of numbers in ascending order. Use sorted().
"""


def sort_list(numbers: list):
	numbers_list = [int(digit) for digit in numbers]
	sorted_list = sorted(numbers_list, reverse=False)

	return sorted_list


sequence_of_numbers = input().split()
print(sort_list(sequence_of_numbers))
