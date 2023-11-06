"""
Write a program that keeps the information about products and their prices. Each product has a name, a price,
and a quantity:
•	If the product doesn't exist yet, add it with its starting quantity.
•	If you receive a product, which already exists, increases its quantity by the input quantity and if its price
is different, replace the price as well.
You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy",
keep adding items. Finally, print all items with their names and the total price of each product.
Input
•	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
•	The product data is always delimited by a single space.
Output
•	Print information about each product in the following format:
"{product_name} -> {total_price}"
•	Format the total price to the 2nd digit after the decimal separator.
"""

products = {}

while True:
    data = input()
    if data == "buy":
        break

    product_name, product_price, product_quantity = data.split()
    product_price = float(product_price)
    product_quantity = int(product_quantity)

    if product_name in products:
        products[product_name]["quantity"] += product_quantity
        if product_price != products[product_name]["price"]:
            products[product_name]["price"] = product_price
    else:
        products[product_name] = {"price": product_price, "quantity": product_quantity}

for product_name, info in products.items():
    total_price = info["price"] * info["quantity"]
    print(f"{product_name} -> {total_price:.2f}")