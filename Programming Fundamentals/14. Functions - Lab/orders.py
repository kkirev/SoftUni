"""
Write a function that calculates the total price of an order and returns it.
The function should receive one of the following products: "coffee", "coke", "water", or "snacks"
and a quantity of the product. The prices for a single piece of each product are:

•	coffee - 1.50
•	water - 1.00
•	coke - 1.40
•	snacks - 2.00

Print the result formatted to the second decimal place.
"""


def price_calc(item, item_count):
	item_price = 0
	if item == "coffee":
		item_price = 1.5
	elif item == "water":
		item_price = 1
	elif item == "coke":
		item_price = 1.4
	elif item == "snacks":
		item_price = 2
	sum = item_price * item_count
	return sum


product = input()
product_quantity = int(input())

final_sum = price_calc(product, product_quantity)
print(f"{final_sum:.2f}")
