"""
https://judge.softuni.org/Contests/Practice/Index/1773#2.

The pirates encounter a huge Man-O-War at sea.
Create a program that tracks the battle and either chooses a winner or prints a stalemate. On the first line,
you will receive the status of the pirate ship, which is a string representing integer sections separated by ">".
On the second line, you will receive the same type of status, but for the warship:
"{section1}>{section2}>{section3}… {sectionn}"
On the third line, you will receive the maximum health capacity a section of the ship can reach.
The following lines represent commands until "Retire":
•	"Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section.
Check if the index is valid and if not, skip the command. If the section breaks (health <= 0) the warship sinks,
print the following and stop the program: "You won! The enemy ship has sunken."
•	"Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that
range (indexes are inclusive). Check if both indexes are valid and if not, skip the command.
If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
"You lost! The pirate ship has sunken."
•	"Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health. Check if
the index is valid and if not, skip the command. The health of the section cannot exceed the maximum health capacity.
•	"Status" - prints the count of all sections of the pirate ship that need repair soon, which are all sections that
are lower than 20% of the maximum health capacity. Print the following:
"{count} sections need repair."
In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections,
in the following format:
"Pirate ship status: {pirateShipSum}
Warship status: {warshipSum}"
Input
•	On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
•	On the 2nd line, you are going to receive the status of the warship
•	On the 3rd line, you will receive the maximum health a section of a ship can reach.
•	On the following lines, until "Retire", you will be receiving commands.
Output
•	Print the output in the format described above.
Constraints
•	The section numbers will be integers in the range [1….1000]
•	The indexes will be integers [-200….200]
•	The damage will be an integer in the range [1….1000]
•	The health will be an integer in the range [1….1000]
"""


def is_index_valid(index: int, sections_count: int) -> bool:
	if 0 <= index < sections_count:
		return True
	return False


def check_health_status(ship_sections: list, max_health: int) -> int:
	need_repair_sections = [int(section) for section in ship_sections if int(section) < 0.2 * max_health]
	return len(need_repair_sections)


pirate_ship_sections = [int(section) for section in input().split(">")]
warship_sections = [int(section) for section in input().split(">")]
max_section_health = int(input())

command = input()
index_boundary_pirate_ship = len(pirate_ship_sections)
index_boundary_warship = len(warship_sections)
battle_end = False

while command != "Retire":

	if command.split()[0] == "Fire":
		index = int(command.split()[1])
		damage = int(command.split()[2])
		if is_index_valid(index, index_boundary_warship):
			warship_sections[index] -= damage	 # submit damage to the warship
			if warship_sections[index] <= 0:
				print(f"You won! The enemy ship has sunken.")
				battle_end = True
		else:
			command = input()	 # skip the command
			continue

	elif command.split()[0] == "Defend":
		start_index = int(command.split()[1])
		end_index = int(command.split()[2])
		damage = int(command.split()[3])
		if is_index_valid(start_index, index_boundary_pirate_ship) and is_index_valid(end_index, index_boundary_pirate_ship):
			for section in range(start_index, end_index + 1):	 # submit damage to the pirate ship
				pirate_ship_sections[section] -= damage
				if int(pirate_ship_sections[section]) <= 0:
					print(f"You lost! The pirate ship has sunken.")
					battle_end = True
					break
		else:
			command = input()	 # skip the command
			continue

	elif command.split()[0] == "Repair":
		index = int(command.split()[1])
		healing_value = int(command.split()[2])
		if is_index_valid(index, index_boundary_warship):
			pirate_ship_sections[index] += healing_value				# heal the pirate ship section with the given
			if int(pirate_ship_sections[index]) > max_section_health: 	# value but do not exceed the max health
				pirate_ship_sections[index] = max_section_health
		else:
			command = input()	 # skip the command
			continue

	elif command.split()[0] == "Status":
		print(f"{check_health_status(pirate_ship_sections, max_section_health)} sections need repair.")

	if battle_end:
		break

	command = input()

if not battle_end:
	print(f"Pirate ship status: {sum(pirate_ship_sections)}\nWarship status: {sum(warship_sections)}")

# judge 90/100