# First try to solve the task

cards = input().split()
current_try = 0

command = input()
while command != "end":
	el_1 = cards[int(command.split()[0])]
	el_2 = cards[int(command.split()[1])]
	current_try += 1
	middle_index = len(cards) // 2

	if int(command.split()[0]) == int(command.split()[1]) \
			or int(command.split()[0]) < 0 \
			or int(command.split()[1]) < 0 \
			or int(command.split()[0]) > len(cards) - 1 \
			or int(command.split()[1]) > len(cards) - 1:
		cards.insert(middle_index, f"-{current_try}a")
		cards.insert(middle_index, f"-{current_try}a")
		print(f"Invalid input! Adding additional elements to the board")

	elif el_1 == el_2:
		cards.remove(el_1)
		cards.remove(el_2)
		print(f"Congrats! You have found matching elements - {el_1}!")

	else:
		print(f"Try again!")

	if len(cards) == 0:
		print(f"You have won in {current_try} turns!")
		break

	command = input()

print(f"Sorry you lose :(\n{" ".join(cards)}")
