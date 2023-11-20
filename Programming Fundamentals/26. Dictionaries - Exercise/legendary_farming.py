"""
You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. However,
it's a tedious process, and it requires quite a bit of farming. The possible items are:
•	"Shadowmourne" - requires 250 Shards
•	"Valanyr" - requires 250 Fragments
•	"Dragonwrath" - requires 250 Motes
"Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
You will be given lines of input in the format:
"{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
Keep track of the key materials - the first one that reaches 250, wins the race. At that point,
you have to print that the corresponding legendary item is obtained.
In the end, print the remaining shards, fragments, motes in the format:
"shards: {number_of_shards}
fragments: {number_of_fragments}
motes: {number_of_motes}"
Finally, print the collected junk items in the order of appearance.

Input
•	Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
Output
•	On the first line, print the obtained item in the format: "{Legendary item} obtained!"
•	On the next three lines, print the remaining key materials
•	On the several final lines, print the junk items
•	All materials should be printed in the format: "{material}: {quantity}"
•	The output should be lowercase, except for the first letter of the legendary
"""

# Ivan Shopov Solution

items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False

while not obtained:
	current_items = input().split()
	for index in range(0, len(current_items), 2):
		value = int(current_items[index])
		item = current_items[index + 1].lower()
		if item not in items:
			items[item] = 0
		items[item] += value
		if items["shards"] >= 250:
			print("Shadowmourne obtained!")
			obtained = True
			items["shards"] -= 250
		elif items["fragments"] >= 250:
			print("Valanyr obtained!")
			items["fragments"] -= 250
			obtained = True
		elif items["motes"] >= 250:
			print("Dragonwrath obtained!")
			items["motes"] -= 250
			obtained = True
		if obtained:
			break

for item, value in items.items():
	print(f"{item}: {value}")

# ---------------------------------------------------------------------------------------------------------------------
# Konstantin Solution - Judge 80/100

# def win_what(material, quantity):
# 	if material == "shards":
# 		win = "Shadowmourne"
# 	elif material == "fragments":
# 		win = "Valanyr"
# 	elif material == "motes":
# 		win = "Dragonwrath"
# 	return win
#
#
# legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
# obtained = False
#
# while not obtained:
# 	materials = input().lower().split()
# 	for index in range(0, len(materials), 2):
# 		quantity = int(materials[index])
# 		material = materials[index + 1]
#
# 		if material not in legendary_items:
# 			legendary_items[material] = quantity
# 		else:
# 			legendary_items[material] += quantity
#
# 		if legendary_items[material] >= 250:
# 			legendary_items[material] -= 250
# 			obtained = True
# 			break
#
# if obtained:
# 	print(f"{win_what(material, legendary_items[material])} obtained!")
# 	for material, quantity in legendary_items.items():
# 		print(f"{material}: {quantity}")

# ---------------------------------------------------------------------------------------------------------------------
# ChatGPT Solution

# legendary_item = ""
# key_materials = {"shards": 0, "fragments": 0, "motes": 0}
# junk_items = {}
#
# while True:
# 	input_line = input().lower().split()
# 	for i in range(0, len(input_line), 2):
# 		quantity = int(input_line[i])
# 		material = input_line[i + 1]
# 		if material in key_materials:
# 			key_materials[material] += quantity
# 			if key_materials[material] >= 250:
# 				legendary_item = material
# 				key_materials[material] -= 250
# 				break
# 		else:
# 			if material not in junk_items:
# 				junk_items[material] = 0
# 			junk_items[material] += quantity
# 	if legendary_item:
# 		break
#
# print(f"{legendary_item.capitalize()} obtained!")
# for material, quantity in key_materials.items():
# 	print(f"{material}: {quantity}")
# for material, quantity in sorted(junk_items.items()):
# 	print(f"{material}: {quantity}")
