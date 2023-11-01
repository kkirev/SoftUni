"""
You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money,
so you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
You will receive a collection of items and a budget in the following format:
{type->price|type->price|type->price……|type->price}
{budget}
The prices for each of the types cannot exceed a specific price, which is given below:

Type			|	Maximum Price
----------------|-----------------
Clothes			|	50.00
Shoes			|	35.00
Accessories		|	20.50

If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have
to reduce the budget with its price value. If you don't have enough money for it, you can't buy it.
Buy as many items as you can.
Next, you should increase the price of each item you have successfully bought by 40% and then sell it.
Calculate if the budget after selling all the items is enough for buying the train ticket.
Input / Constraints
•	On the 1st line, you will receive the items with their prices in the format described above – real numbers
in the range [0.00……1000.00]
•	On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
Output
•	First, print the list with the bought item’s new prices, formatted to the second decimal point in the
following format:
"{price1} {price2} {price3} … {priceN}"
•	Second, print the profit, formatted to the second decimal point in the following format:
"Profit: {profit}"
•	Finally:
o	If the budget is enough for buying the train ticket, print: "Hello, France!"
o	Otherwise, print: "Not enough money."
"""


items = input().split("|")
initial_budget = float(input())
budget = initial_budget

items_for_sell = []
income_sum = []
prices_with_markup = []

for item in items:
	item_type, item_price = item.split("->")
	item_price = float(item_price)
	if item_type == "Clothes" and item_price <= 50 and budget >= item_price:
		budget -= item_price
		items_for_sell.append(item_type)
		income_sum.append(item_price)
		prices_with_markup.append(f"{item_price * 1.4:.2f}")

	elif item_type == "Shoes" and item_price <= 35 and budget >= item_price:
		budget -= item_price
		items_for_sell.append(item_type)
		income_sum.append(item_price)
		prices_with_markup.append(f"{item_price * 1.4:.2f}")

	elif item_type == "Accessories" and item_price <= 20.5 and budget >= item_price:
		budget -= item_price
		items_for_sell.append(item_type)
		income_sum.append(item_price)
		prices_with_markup.append(f"{item_price * 1.4:.2f}")

markup_sum = sum([float(price) for price in prices_with_markup])
income_sum = sum([float(price) for price in income_sum])
profit = markup_sum - income_sum

print(*prices_with_markup, sep=" ")
print(f"Profit: {profit:.2f}")

if initial_budget + profit >= 150:
	print("Hello, France!")
else:
	print("Not enough money.")