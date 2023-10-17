"""
Write a program that reads a single string with numbers separated by comma and space ", ".
Print the indices of all even numbers.
"""

numbers_as_string = input().split(", ")
numbers_as_integers = [int(char) for char in numbers_as_string]

numbers_index = [index for index in range(len(numbers_as_integers)) if numbers_as_integers[index] % 2 == 0]

print(numbers_index)