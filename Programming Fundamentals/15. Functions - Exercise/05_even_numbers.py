"""
Write a program that receives a sequence of numbers (integers) separated by a single space.
It should print a list of only the even numbers. Use filter().
"""


# def even_numbers(numbers: str):
# 	even_list = [int(digit) for digit in numbers if int(digit) % 2 == 0]
# 	return even_list
#
#
# sequence_of_numbers = input().split()
# print(even_numbers(sequence_of_numbers))

# ----------------------------------------------------------------------------------------------------------------------

sequence_of_numbers = input().split()
sequence_as_digits = [int(digit) for digit in sequence_of_numbers]

is_even = lambda x: x % 2 == 0
even_list = list(filter(is_even, sequence_as_digits))

print(even_list)