item_types = ["Clothes", "Shoes", "Accessories"]
item_prices = [50.00, 35.00, 20.50]
bought_items_prices = []

items_info = input().split("|")
initial_budget = float(input())

for item in items_info:
    item_info = item.split("->")
    item_type, item_price = item_info[0], float(item_info[1])
    if item_type in item_types:
        type_index = item_types.index(item_type)
        if item_price <= item_prices[type_index] and item_price <= initial_budget:
            bought_items_prices.append(item_price)
            initial_budget -= item_price

updated_prices = []
for price in bought_items_prices:
    updated_price = price + price * 0.4
    updated_prices.append(updated_price)

print(" ".join([f"{price:.2f}" for price in updated_prices]))
profit = sum(updated_prices) - sum(bought_items_prices)
print(f"Profit: {profit:.2f}")

if sum(updated_prices) >= 150:
    print("Hello, France!")
else:
    print("Not enough money")
