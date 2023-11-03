pocket_money_per_day = float(input())
sales_money_per_day = float(input())
total_expenses = float(input())
gift_price = float(input())


total_saved_money = 5 * (pocket_money_per_day + sales_money_per_day) - total_expenses
diff = abs(total_saved_money - gift_price)

if total_saved_money >= gift_price:
    print(f'Profit: {total_saved_money:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {diff:.2f} BGN.')
