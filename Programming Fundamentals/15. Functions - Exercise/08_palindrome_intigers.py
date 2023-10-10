"""
A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
Write a function that receives a list of positive integers, separated by comma and space ", ".
The function should check if each integer is a palindrome - True or False. Print the result.
"""


# def palindrome_check(numbers: list):
# 	# int_list = [int(num) for num in numbers]
# 	for number in numbers:
# 		current_list = list(number)
# 		reversed_list = list(reversed(current_list))
# 		if current_list == reversed_list:
# 			print(True)
# 		else:
# 			print(False)
#
#
# sequence_of_numbers = input().split(", ")
# palindrome_check(sequence_of_numbers)
#
# # -------------------------------------------------------------------------------------------------------------------
#
# def palindrome_check(number_as_string: str) -> bool:
# 	if number_as_string == number_as_string[:: -1]:
# 		return True
# 	return False
#
# sequence_of_numbers = input().split(", ")
#
# for number in sequence_of_numbers:
# 	print(palindrome_check(number))
#
# ---------------------------------------------------------------------------------------------------------------------


def palindrome_check(number_as_string: str) -> bool:
	return number_as_string == number_as_string[:: -1]


sequence_of_numbers = input().split(", ")

for number in sequence_of_numbers:
	print(palindrome_check(number))