"""Write a program that reads a sequence of strings, separated by a single space. Each string should be
repeated N times, where N is the length of the string. Print the final strings concatenated into one string.
"""

text_sequences = input().split()
repeated_text = ""

for text in text_sequences:
	repeated_text += text * len(text)

print(repeated_text)