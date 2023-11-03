"""
You will receive three integer numbers.

Write functions named:
•	sum_numbers() that returns the sum of the first two integers
•	subtract() that returns the difference between the returned result of the first function and the third integer
Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.

Print the result of the subtract() function on the console.
"""


def sum_numbers(first, second):
	return first + second


def subtract(sum_result, third):
	return sum_result - third


def add_and_subtract(first, second, third):
	sum_result = sum_numbers(first_num, second_num)
	final_result = subtract(sum_result, third_num)
	return final_result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))




