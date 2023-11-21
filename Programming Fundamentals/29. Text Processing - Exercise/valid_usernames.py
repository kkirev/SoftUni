"""
Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on
separate lines.
A valid username:
•	has length between 3 and 16 characters inclusive
•	can contain only letters, numbers, hyphens, and underscores
•	has no redundant symbols before, after, or in between
"""


def valid_length(some_username):
	if 3 <= len(some_username) <= 16:
		return True
	return False


def valid_content(some_username):
	for char in some_username:
		if not (char.isalnum() or char == "-" or char == "_"):
			return False
	return True


def no_redundant_symbols(some_username):
	if " " in some_username:
		return False
	return True


def valid_username(some_username):
	if valid_length(some_username) and valid_content(some_username) and no_redundant_symbols(some_username):
		return True


usernames = input().split(", ")
valid_usernames = []

for username in usernames:
	if valid_username(username):
		valid_usernames.append(username)

print(*valid_usernames, sep="\n")