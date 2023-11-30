"""
https://judge.softuni.org/Contests/Compete/Index/1743#1

Write a program that receives strings on different lines and extracts only the numbers.
Print all extracted numbers on a single line, separated by a single space.
"""

import re

text = input()
while text:
	pattern = r"\d+"
	matches = re.findall(pattern, text)
	if matches:
		print(*matches, end=' ')

	text = input()