"""
Using comprehension, write a program that receives some text, separated by space, and take only those words whose
length is even. Print each word on a new line.
"""

some_text = input().split()
even_letter_count = [word for word in some_text if len(word) % 2 == 0]

print(*even_letter_count, sep="\n")
# print("/n".join(even_letter_count))