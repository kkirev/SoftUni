square_meters = float(input())
price_per_meter = float(7.61)
total_price = square_meters * price_per_meter
discount = 0.18 * total_price
print(f"The final price is: {total_price - discount} lv.")
print(f"The discount is: {discount} lv.")