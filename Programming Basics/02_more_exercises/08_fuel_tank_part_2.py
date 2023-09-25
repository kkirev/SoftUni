fuel_type = input()
fuel_amount = float(input())
club_card = input()

price = 0
if fuel_type == "Gasoline":
     price = 2.22
     if club_card == "Yes":
         price -= 0.18
elif fuel_type == "Diesel":
     price = 2.33
     if club_card == "Yes":
         price -= 0.12
elif fuel_type == "Gas":
     price = 0.93
     if club_card == "Yes":
         price -= 0.08

final_bill = fuel_amount * price

if 20 <= fuel_amount <= 25:
    final_bill *= 0.92
elif fuel_amount > 25:
    final_bill *= 0.9

print(f'{final_bill:.2f} lv.')