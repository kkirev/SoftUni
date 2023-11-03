"""
Write a program that receives a single word, reverses it, and prints it.
"""

word = input()

for letter in range(len(word) - 1, -1, -1):
    print(word[letter], end='')

# word = input()
#     print(word[::-1])