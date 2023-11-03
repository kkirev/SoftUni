"""
Write a program that receives a sequence of numbers (integers) separated by a single space. It should print
the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
The output should be as follows:

•	On the first line: "The minimum number is {minimum number}"
•	On the second line: "The maximum number is {maximum number}"
•	On the third line: "The sum number is: {sum of all numbers}"
"""


def min_max_sum(numbers: list):
	int_list = [int(num) for num in numbers]
	min_number = min(int_list)
	max_number = max(int_list)
	all_numbers_sum = sum(int_list)
	return min_number, max_number, all_numbers_sum


sequence_of_numbers = input().split()
min_number, max_number, all_numbers_sum = min_max_sum(sequence_of_numbers)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {all_numbers_sum}")
