"""
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2031#1.

It's the end of the week, and it is time for you to go shopping, so you need to create a shopping list first.
Input
You will receive an initial list with groceries separated by an exclamation mark "!".
After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
•	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
•	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise,
skip this command.
•	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one.
Otherwise, skip this command.
•	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the
end of the list. Otherwise, skip this command.
Constraints
•	There won't be any duplicate items in the initial list
"""

groceries_list = input().split("!")

command = input()
while command != "Go Shopping!":
	key_word = command.split()[0]

	if key_word == "Urgent":
		item = command.split()[1]
		if item in groceries_list:
			command = input()
			continue
		else:
			groceries_list.insert(0, item)

	elif key_word == "Unnecessary":
		item = command.split()[1]
		if item in groceries_list:
			groceries_list.remove(item)
		else:
			command = input()
			continue

	elif key_word == "Correct":
		item_to_remove = command.split()[1]
		item_to_add = command.split()[2]
		if item_to_remove in groceries_list:
			index = groceries_list.index(item_to_remove)
			groceries_list.pop(index)
			groceries_list.insert(index, item_to_add)
		else:
			command = input()
			continue

	elif key_word == "Rearrange":
		item = command.split()[1]
		if item in groceries_list:
			groceries_list.remove(item)
			groceries_list.append(item)
		else:
			command = input()
			continue

	command = input()

print(*groceries_list, sep=", ")
