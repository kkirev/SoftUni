products = {}

command = input()
while command != "buy":
	product, price, quantity = command.split()

	if product not in products:
		products[product] = 0
	products[product] = price, quantity

	command = input()