"""
Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals in
the zoo. The __init__ method should only receive the name of the zoo. There you should also create 3 empty
lists (mammals, fishes, birds). The class should also have 2 more methods:
•	add_animal(species, name) - based on the species, adds the name to the corresponding list
•	get_info(species) - based on the species returns a string in the following format:
"{Species} in {zoo_name}: {names}
Total animals: {total_animals}"
On the first line, you will receive the name of the zoo. On the second line, you will receive number n.
On the following n lines you will receive animal info in the format: "{species} {name}".
Add the animal to the zoo to the corresponding list. The species could be "mammal", "fish", or "bird".
On the final line, you will receive a species.

At the end, print the info for that species and the total count of animals in the zoo.
"""


class Zoo():
	__animals = 0

	def __init__(self, name):
		self.name = name
		self.mammals = []
		self.fishes = []
		self.birds = []

	def add_animal(self, species, name):
		if species == "mammal":
			self.mammals.append(name)
		elif species == "fish":
			self.fishes.append(name)
		elif species == "bird":
			self.birds.append(name)
		Zoo.__animals += 1

	def get_info(self, species):
		print_string = ""
		if species == "mammal":
			print_string += f"Mammals in {self.name}: {', '.join(self.mammals)}"
		elif species == "fish":
			print_string += f"Fishes in {self.name}: {', '.join(self.fishes)}"
		elif species == "bird":
			print_string += f"Birds in {self.name}: {', '.join(self.birds)}"
		print_string += f"\nTotal animals: {Zoo.__animals}"
		return print_string


zoo_name = input()
zoo_object = Zoo(zoo_name)
animals_count = int(input())

for animal in range(animals_count):
	species, animal_type = input().split()
	zoo_object.add_animal(species, animal_type)

searched_species = input()
print(zoo_object.get_info(searched_species))