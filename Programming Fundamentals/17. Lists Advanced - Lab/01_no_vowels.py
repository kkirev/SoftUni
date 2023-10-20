"""
Using comprehension, write a program that receives a text and removes all its vowels, case insensitive. Print the
new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.
"""

text = input()
vowels_to_remove = ['a', 'o', 'u', 'e', 'i']

result = [letter for letter in text if letter.lower() not in vowels_to_remove]

print("".join(result))