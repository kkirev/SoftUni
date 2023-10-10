"""
Write a function that receives two characters and returns a single string with all the characters in between them
(according to the ASCII code), separated by a single space.
Print the result on the console.
"""


def chars_betwen(begin, end):
	result = [chr(digit) for digit in range(ord(begin) + 1, ord(end))]
	# result = []
	# for digit in range(ord(begin) + 1, ord(end)):
	# 	result_list.append(chr(digit))
	return " ".join(result)


first_char = input()
second_char = input()

print(chars_betwen(first_char, second_char))