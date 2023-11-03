"""
Write a program that prints all elements from a given sequence of words that occur an odd number of
times (case-insensitive) in it.
•	Words are given on a single line, space-separated.
•	Print the result elements in lowercase, in their order of appearance.
"""

words_keys = input().lower().split() # words_keys = [key.lower() for key in input().split()]
defaults = 0

occurrences = dict.fromkeys(words_keys, defaults)

for word in words_keys:
	# occurrences[word] = words_keys.count(word)
	occurrences[word] += 1

for word, count in occurrences.items():
	if count % 2 != 0:
		print(word, end=" ")