events_list = input().split("|")
initial_energy = 100
initial_coins = 100

all_done = True
for event in events_list:
	event_items = event.split("-")
	event_type = event_items[0]
	event_value = int(event_items[1])

	if event_type == "rest":
		current_energy = initial_energy
		initial_energy += event_value
		if initial_energy > 100:
			initial_energy = 100
		gained_energy = initial_energy - current_energy
		print(f"You gained {gained_energy} energy.")
		print(f"Current energy: {initial_energy}.")

	elif event_type == "order":
		if initial_energy >= 30:
			initial_energy -= 30
			initial_coins += event_value
			print(f"You earned {event_value} coins.")
		else:
			initial_energy += 50
			print(f"You had to rest!")

	else:
		ingredient = event_type
		if initial_coins >= event_value:
			initial_coins -= event_value
			print(f"You bought {ingredient}.")
		else:
			print(f"Closed! Cannot afford {ingredient}.")
			all_done = False
			break

if all_done:
	print("Day completed!")
	print(f"Coins: {initial_coins}")
	print(f"Energy: {initial_energy}")