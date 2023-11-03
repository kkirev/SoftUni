"""
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2517#2.

Write a program that recreates the Memory game.
On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin.
Until the player receives "end" from the console, you will receive strings with two integers separated by a space,
representing the indexes of elements in the sequence.
If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence,
you should add two matching elements at the middle of the sequence in the following format:
"-{number of moves until now}a"
Then print this message on the console:
"Invalid input! Adding additional elements to the board"
Input
•	On the first line, you will receive a sequence of elements
•	On the following lines, you will receive integers until the command "end"
Output
•	Every time the player hit two matching elements, you should remove them from the sequence and print on the
console the following message:
"Congrats! You have found matching elements - ${element}!"
•	If the player hit two different elements, you should print on the console the following message:
"Try again!"
•	If the player hit all matching elements before he receives "end" from the console,
you should print on the console the following message:
"You have won in {number of moves until now} turns!"
•	If the player receives "end" before he hits all matching elements,
you should print on the console the following message:
"Sorry you lose :(
{the current sequence's state}"
Constraints
•	All elements in the sequence will always have a matching element.
"""


def is_index_in_range(index, cards_count):
	if 0 <= index < cards_count:
		return True
	return False


def check_indices_are_valid(index_1, index_2, cards_count):
	if is_index_in_range(index_1, cards_count) and is_index_in_range(index_2, cards_count) and index_1 != index_2:
		return True
	return False


cards = input().split()
moves_counter = 0

command = input()
while command != "end":
	moves_counter += 1
	index_1, index_2 = [int(el) for el in command.split()]

	if check_indices_are_valid(index_1, index_2, len(cards)):
		if cards[index_1] == cards[index_2]:
			element = cards[index_1]
			cards.remove(element)
			cards.remove(element)
			print(f"Congrats! You have found matching elements - {element}!")
		else:
			print(f"Try again!")
	else:
		#punisment
		element_to_add = f"-{moves_counter}a"
		index = len(cards) // 2
		cards.insert(index, element_to_add)
		cards.insert(index, element_to_add)
		print(f"Invalid input! Adding additional elements to the board")

	if not cards:
		print(f"You have won in {moves_counter} turns!")
		exit(0)

	command = input()

print(f"Sorry you lose :(")
print(*cards, sep=" ")

