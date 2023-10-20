"""
You will be receiving to-do notes until you get the command "End".
The notes will be in the format: "{importance}-{note}".
Return a list containing all to-do notes sorted by importance in ascending order.
The importance value will always be an integer between 1 and 10 (inclusive).
"""

command = input()
to_do_list = [0] * 10

while command != "End":
	priority, note = command.split("-")
	priority = int(priority)
	index = priority - 1
	to_do_list[index] = note

	command = input()

print([note for note in to_do_list if note != 0])