"""
Write a program that receives info from the console about people and their phone numbers.
Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already exists
in the phonebook, update its number.
After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of contact
by name and print its details in the format: "{name} -> {number}".
In case the contact isn't found, print: "Contact {name} does not exist."
"""

phonebook = {}
entry = input()

while "-" in entry:
	name, phone_number = entry.split("-")
	phonebook[name] = phone_number
	entry = input()

searches_numbers = int(entry)

for search in range(searches_numbers):
	searched_name = input()
	if searched_name in phonebook.keys():
		print(f"{searched_name} -> {phonebook[searched_name]}")
	else:
		print(f"Contact {searched_name} does not exist.")
