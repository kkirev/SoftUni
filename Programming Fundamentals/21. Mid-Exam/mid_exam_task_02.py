travel_route = input().split("||")
initial_fuel = int(input())
initial_ammunition = int(input())

mission_completed = False

for command in travel_route:

	if command == "Titan":
		mission_completed = True
		break
	else:
		action, action_value = command.split()
		# action = command.split()[0]
		# action_value = command.split()[1]
		action_value = int(action_value)

	if action == "Travel":
		initial_fuel -= action_value
		print(f"The spaceship travelled {action_value} light-years.")

	elif action == "Enemy":
		if initial_ammunition >= action_value:
			initial_ammunition -= action_value
			print(f"An enemy with {action_value} armour is defeated.")
		else:
			if initial_fuel >= action_value * 2:
				initial_fuel -= action_value * 2
				print(f"An enemy with {action_value} armour is outmaneuvered.")
			else:
				mission_completed = False
				break

	elif action == "Repair":
		initial_ammunition += action_value
		print(f"Ammunitions added: {action_value * 2}.")
		print(f"Fuel added: {action_value}.")

if mission_completed:
	print(f"You have reached Titan, all passengers are safe.")
else:
	print(f"Mission failed.")
