"""
Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
and prints all the positive, negative, even, and odd numbers on separate lines as shown below.

Note: Zero is counted for a positive number
"""


def positive_nums(numbers: list):
	return ", ".join([number for number in numbers if int(number) >= 0])


def negative_nums(numbers: list):
	return ", ".join([number for number in numbers if int(number) < 0])


def even_nums(numbers: list):
	return ", ".join([number for number in numbers if int(number) % 2 == 0])


def odd_nums(numbers: list):
	return ", ".join([number for number in numbers if int(number) % 2 != 0])


numbers = input().split(", ")

print(f"Positive: {positive_nums(numbers)}")
print(f"Negative: {negative_nums(numbers)}")
print(f"Even: {even_nums(numbers)}")
print(f"Odd: {odd_nums(numbers)}")


# WHY JUDGE DO NOT ACCEPT THIS SOLUTION?
#
# numbers = input().split(", ")
#
# positive_numbers = [number for number in numbers if int(number) >= 0]
# negative_numbers = [number for number in numbers if int(number) < 0]
# even_numbers = [number for number in numbers if int(number) % 2 == 0]
# odd_numbers = [number for number in numbers if int(number) % 2 != 0]
#
# print(f"Positive: {", ".join(positive_numbers)}")
# print(f"Negative: {", ".join(negative_numbers)}")
# print(f"Even: {", ".join(even_numbers)}")
# print(f"Odd: {", ".join(odd_numbers)}")
