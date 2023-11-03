"""
You will be given two sequences of strings, separated by ", ". Print a new list containing only the strings from
the first input line, which are substrings of any string in the second input line
"""

first_sequence = input().split(", ")
second_sequence = input().split(", ")
# result = []
#
# for word_part in first_sequence:
# 	for word in second_sequence:
# 		if word_part in word and word_part not in result:
# 			result.append(word_part)

result = [word_part for word_part in first_sequence if any(word_part in word for word in second_sequence)]

print(result)