"""
Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
Use round().
"""

# def round_it(list):
# 	list = [round(number) for number in list]
# 	return list
#
#
# numbers = [float(number) for number in input().split()]
# print(round_it(numbers))

numbers = input().split()

for number in numbers:
	numbers_as_floats = []
	numbers_as_floats.append(float(number))

def round_it(list):
	rounded_list = []
	for number in list:
		rounded_list.append(round(number))
	return rounded_list


print(round_it(numbers_as_floats))