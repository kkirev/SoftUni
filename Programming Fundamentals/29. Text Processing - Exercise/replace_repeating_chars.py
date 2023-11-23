"""
Write a program that reads a string from the console and replaces any sequence of the same letters with a single
corresponding letter.
"""

text = input()
cleaned_text = ""
last_char = ""

for char in text:
	if char != last_char:
		cleaned_text += char
	last_char = char
print(cleaned_text)
