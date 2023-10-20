"""
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2028#0.

You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's rooms.
Each room is separated with '|' (vertical bar): "room1|room2|room3…"
Each room contains a command and a number, separated by space. The command can be:
•	"potion"
o	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
o	First print: "You healed for {amount} hp."
o	After that, print your current health: "Current health: {health} hp."
•	"chest"
o	You've found some bitcoins, the number in the second part.
o	Print: "You found {amount} bitcoins."
•	In any other case, you are facing a monster, which you will fight. The second part of the room contains the attack
of the monster. You should remove the monster's attack from your health.
o	If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
o	If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room you've manage
to reach: "Best room: {room}"
If you managed to go through all the rooms in the dungeon, print on the following three lines:
"You've made it!"
"Bitcoins: {bitcoins}"
"Health: {health}"
Input / Constraints
You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".
Output
Print the corresponding messages described above.
"""

dungeons_rooms = input().split("|")
initial_health = 100
initial_bitcoins = 0
current_health = 0
room_counter = 0

for room in dungeons_rooms:
	room_counter += 1
	room_command = room.split()[0]
	room_value = room.split()[1]

	if room_command == "potion":
		current_health = initial_health
		initial_health += int(room_value)
		if initial_health > 100:
			initial_health = 100
		used_healing = initial_health - current_health
		print(f"You healed for {used_healing} hp.")
		print(f"Current health: {initial_health} hp.")

	elif room_command == "chest":
		initial_bitcoins += int(room_value)
		print(f"You found {room_value} bitcoins.")

	else:
		initial_health -= int(room_value)
		if initial_health > 0:
			print(f"You slayed {room_command}.")
		else:
			print(f"You died! Killed by {room_command}.")
			print(f"Best room: {room_counter}")
			break

if initial_health > 0:
	print(f"You've made it!")
	print(f"Bitcoins: {initial_bitcoins}")
	print(f"Health: {initial_health}")
