"""
On the first line, you will receive words separated by a single space. On the second line, you will
receive a palindrome. First, you should print a list containing all the found palindromes in the sequence. Then,
you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".
"""

words = input().split()
palindrome_word = input()
palindroime_counter = 0

# palindrome_list = [word for word in words if list(word) == reversed(list(word))]
palindrome_list = []

for word in words:
	if list(word) == list(reversed(word)):
		if palindrome_word == word:
			palindroime_counter += 1
		palindrome_list.append(word)

print(palindrome_list)
print(f"Found palindrome {palindroime_counter} times")
