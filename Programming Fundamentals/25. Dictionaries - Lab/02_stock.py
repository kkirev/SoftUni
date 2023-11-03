"""
After you have completed your first task, your boss decides to give you another one right away.
Now not only you have to keep track of the stock, but also you should answer customers if you have some
products in stock or not.
You will be given key-value pairs of products and quantities (on a single line separated by space).
On the following line, you will be given products to search for. Check for each product. You have 2 possibilities:
•	If you have the product, print "We have {quantity} of {product} left".
•	Otherwise, print "Sorry, we don't have {product}".
"""

data = input().split()
products_in_stock = {}

for index in range(0, len(data), 2):
	key = data[index]
	product = key
	value = int(data[index + 1])
	quantity = value
	products_in_stock[product] = quantity

searched_products = input().split()
for searched_product in searched_products:
	if searched_product in products_in_stock:
		print(f"We have {products_in_stock[searched_product]} of {searched_product} left")
	else:
		print(f"Sorry, we don't have {searched_product}")
