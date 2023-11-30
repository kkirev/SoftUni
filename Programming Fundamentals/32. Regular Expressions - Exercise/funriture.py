"""
https://judge.softuni.org/Contests/Compete/Index/1743#4

Write a program that calculates the total cost of bought furniture. You will be given information about each purchase
on separate lines until you receive the command "Purchase". Valid information should
be in the format: ">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point or integer number.
You should store the names of the furniture and the total price.
In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
"Bought furniture:
{1st name}
{2nd name}
…
{N name}
Total money spend: {total_cost}"
"""

import re

bought_furniture = []
total_cost = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"

command = input()
while command != "Purchase":
	match = re.search(pattern, command)
	if match:
		furniture, price, quantity = match.groups()
		bought_furniture.append(furniture)
		total_cost += float(price) * int(quantity)
	command = input()

print("Bought furniture:")
for furniture in bought_furniture:
	print(furniture)
print(f"Total money spend: {total_cost:.2f}")

