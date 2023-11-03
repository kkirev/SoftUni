"""
As a young baker, you are baking the bread out of the bakery.
You have initial energy 100 and initial coins 100. You will be given a string representing the working day events.
Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")
•	If the event is "rest":
o	You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100).
Print: "You gained {gained_energy} energy.".
o	After that, print your current energy: "Current energy: {current_energy}.".
•	If the event is "order":
o	You've earned some coins (the number in the second part).
o	Each time you get an order, your energy decreases by 30 points.
	If you have the energy to complete the order, print: "You earned {earned} coins.".
	Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
•	In any other case, you have an ingredient you should buy. The second part of the event contains the coins you
should spend.
o	If you have enough money, you should buy the ingredient and print:
"You bought {ingredient}."
o	Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
If you managed to handle all events throughout the day, print on the following 3 lines:
"Day completed!"
"Coins: {coins}"
"Energy: {energy}"
Input / Constraints
You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
"event1|event2| … eventN".
Each event contains an event name or an ingredient and a number,
separated by a dash in the format: "{event/ingredient}-{number}"
Output
Print the corresponding messages described above.
"""

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