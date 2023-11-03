"""
Your first task at your new job is to create a table of the stock in a bakery,
and you really don't want to fail on your first day at work.
You will receive a single line containing some food (keys) and quantities (values).
They will be separated by a single space (the first element is the key, the second – the value, and so on).
Create a dictionary with all the keys and values and print it on the console.

Hint
Let us start with reading the input and creating an empty dictionary:
"""

products = {}
data = input().split()

for index in range(0, len(data), 2):
	key = data[index]
	value = int(data[index + 1])
	products[key] = value

print(products)
