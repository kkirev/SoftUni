from math import floor, ceil

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cacti_count = int(input())
gift_price = float(input())

magnolias_price = 3.25
hyacinths_price = 4 #зюмбюли
roses_price = 3.5
cacti_price = 8 #кактуси - many cactus plants

total_income = magnolias_count * magnolias_price + hyacinths_count * hyacinths_price \
               + roses_count * roses_price + cacti_count * cacti_price
tax_profit = total_income * 0.05
final_profit = total_income - tax_profit
difference = abs(final_profit - gift_price)

if final_profit >= gift_price:
    print(f'She is left with {floor(difference)} leva.')
else:
    print(f'She will have to borrow {ceil(difference)} leva.')