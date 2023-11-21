"""Write a program that receives a single string. On the first line, print all the digits found in the string,
on the second – all the letters, and on the third – all the other characters. There will always be at least one digit,
one letter, and one other character.
"""

text = input()

digits = ""
letters = ""
others = ""

for char in text:
	if char.isdigit():
		digits += char
	elif char.isalpha():
		letters += char
	else:
		others += char

print(digits)
print(letters)
print(others)