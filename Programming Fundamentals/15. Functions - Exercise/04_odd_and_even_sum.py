"""
You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a
given number. The result should be returned as a single string in the format:

"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

Print the result of the function on the console.
"""


def odd_and_even_sum(number: str):
	str_list_from_num = list(number)
	# sum_of_odd_digits = 0
	# sum_of_even_digits = 0
	# for digit in str_list_from_num:
	# 	if int(digit) % 2 != 0:
	# 		sum_of_odd_digits += int(digit)
	# 	else:
	# 		sum_of_even_digits += int(digit)
	list_of_odd_digits = [int(digit) for digit in str_list_from_num if int(digit) % 2 != 0]
	sum_of_odd_digits = sum(list_of_odd_digits)
	list_of_even_digits = [int(digit) for digit in str_list_from_num if int(digit) % 2 == 0]
	sum_of_even_digits = sum(list_of_even_digits)
	return sum_of_odd_digits, sum_of_even_digits


input_num = input()

sum_of_odd_digits, sum_of_even_digits = odd_and_even_sum(input_num)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
