"""
Write a program that counts all characters in a string except for space (" ").
Print all the occurrences in the following format:
"{char} -> {occurrences}"
"""

text = [char for char in input() if char != " "]
chars_count = {}

for char in text:
	if char not in chars_count.keys():
		chars_count[char] = 0
	chars_count[char] += 1

for char, occurrences in chars_count.items():
	print(f"{char} -> {occurrences}")
	# print(char, "->", occurrences)

# ---------------------------------------------------------------------------------------------------------------------

# text = input()
# char_count = {}
#
# for char in text:
# 	if char != ' ':
# 		if char in char_count:
# 			char_count[char] += 1
# 		else:
# 			char_count[char] = 1
#
# for char, count in char_count.items():
# 	print(f"{char} -> {count}")

# ---------------------------------------------------------------------------------------------------------------------

# text = input().replace(" ", "")
# char_count = {}
#
# for char in text:
#     char_count[char] = char_count.get(char, 0) + 1

# for key, value in char_count.items():
#     print(f"{key} -> {value}")

# ---------------------------------------------------------------------------------------------------------------------
