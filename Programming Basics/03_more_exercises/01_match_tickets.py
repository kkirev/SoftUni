budget = float(input())
category = input()
fans_count = int(input())

transport_cost = 0
tickets_price = 0

if 1 <= fans_count <= 4:
    transport_cost = budget * 0.75
elif 5 <= fans_count <= 9:
    transport_cost = budget *  0.6
elif 10 <= fans_count <= 24:
    transport_cost = budget * 0.5
elif 25 <= fans_count <= 49:
    transport_cost = budget * 0.4
elif fans_count >= 50:
    transport_cost = budget * 0.25

money_for_tickets = budget - transport_cost

if category == 'VIP':
    tickets_price = 499.99 * fans_count
    if money_for_tickets >= tickets_price:
        print(f'Yes! You have {abs(money_for_tickets - tickets_price):.2f} leva left.')
    else:
        print(f'Not enough money! You need {abs(money_for_tickets - tickets_price):.2f} leva.')
elif category == 'Normal':
    tickets_price = 249.99 * fans_count
    if money_for_tickets >= tickets_price:
        print(f'Yes! You have {abs(money_for_tickets - tickets_price):.2f} leva left.')
    else:
        print(f'Not enough money! You need {abs(money_for_tickets - tickets_price):.2f} leva.')