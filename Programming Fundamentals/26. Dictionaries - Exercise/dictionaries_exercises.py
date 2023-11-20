# 1. Count Chars in a String
# text = [char for char in input() if char != " "]
# chars_count = {}
# for char in text:
# 	if char not in chars_count:
# 		chars_count[char] = 0
# 	chars_count[char] += 1
# for char, occurrences in chars_count.items():
# 	print(f"{char} -> {occurrences}")
# ---------------------------------------------------------------------------------------------------------------------
# 2. A Miner Task
# resources = {}
# counter = 1
#
# current_resource = input()
# while current_resource != "stop":
# 	if current_resource not in resources.keys():
# 		resources[current_resource] = 0
# 	current_quantity = int(input())
# 	resources[current_resource] += current_quantity
#
# 	current_resource = input()
#
# for resource, quantity in resources.items():
# 	print(f"{resource} -> {quantity}")
# ---------------------------------------------------------------------------------------------------------------------
# 3. Capitals
# countries = input().split(", ")
# capitals = input().split(", ")

# zip_dict = dict(zip(countries, capitals)) 											# Solution 1
# zip_dict = {country: capital for country, capital in zip(countries, capitals)} 		# Solution 2
# zip_dict = {countries[index]: capitals[index] for index in range(len(countries))} 	# Solution 3

# for country, capital in zip_dict.items():
# 	print(f"{country} -> {capital}")
# ---------------------------------------------------------------------------------------------------------------------
# 4. Phonebook
# entry = input()
# phonebook = {}
#
# while "-" in entry:
# 	name, phone_number = entry.split("-")
# 	if name not in phonebook.keys():
# 		phonebook[name] = 0
# 	phonebook[name] = phone_number
# 	entry = input()
#
# searches_number = int(entry)
# for search in range(searches_number):
# 	searched_name = input()
# 	if searched_name not in phonebook.keys():
# 		print(f"Contact {searched_name} does not exist.")
# 	else:
# 		print(f"{searched_name} -> {phone_number}")
# ---------------------------------------------------------------------------------------------------------------------
# 5.Legendary Farming
def win_what(material, quantity):
	if material == "shards":
		win = "Shadowmourne"
	elif material == "fragments":
		win = "Valanyr"
	elif material == "motes":
		win = "Dragonwrath"
	return win


legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False

while not obtained:
	materials = input().lower().split()
	for index in range(0, len(materials), 2):
		quantity = int(materials[index])
		material = materials[index + 1]

		if material not in legendary_items:
			legendary_items[material] = quantity
		else:
			legendary_items[material] += quantity

		if legendary_items[material] >= 250:
			legendary_items[material] -= 250
			obtained = True
			break

if obtained:
	print(f"{win_what(material, legendary_items[material])} obtained!")
	for material, quantity in legendary_items.items():
		print(f"{material}: {quantity}")
# Judge 80/100
# ---------------------------------------------------------------------------------------------------------------------
# 6. Orders
