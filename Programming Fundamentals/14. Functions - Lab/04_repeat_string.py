"""
Write a function that receives a string and a counter n. The function should return a new string – the result of
repeating the old string n times. Print the result of the function. Try using lambda.
"""


def str_repeater(str, count):
	result = str * count
	return result


string = input()
repeat_count = int(input())
print(str_repeater(string, repeat_count))
