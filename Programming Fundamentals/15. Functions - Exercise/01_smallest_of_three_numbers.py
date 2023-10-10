"""
You will receive three integer numbers.
Write functions named:
•	sum_numbers() that returns the sum of the first two integers
•	subtract() that returns the difference between the returned result of the first function and the third integer
Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
Print the result of the subtract() function on the console.
"""


def smallest_num(a, b, c) -> int and int:
	numbers = [a, b, c]
	smallest = min(numbers)
	return smallest


first_num = int(input())
second_num = int(input())
third_num = int(input())

smallest = smallest_num(first_num, second_num, third_num)
print(smallest)