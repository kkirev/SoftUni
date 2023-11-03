"""
Write a function that receives two integer numbers. Calculate the factorial of each number.
Divide the first result by the second and print the division formatted to the second decimal point.
"""


def factorial_num(number: int) -> int:
	for current_num in range(1, number):
		number *= current_num
	return number #initial number factorial -> number


first_num = int(input())
second_num = int(input())

first_num_factorial = factorial_num(first_num)
second_num_factorial = factorial_num(second_num)

result = first_num_factorial / second_num_factorial

print(f"{result:.2f}")
