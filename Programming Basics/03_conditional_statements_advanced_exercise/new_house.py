flowers_kind = input()
flowers_count = int(input())
budget = int(input())

price = 0
discount = 0

if flowers_kind == 'Roses':
    price = 5
    if flowers_count > 80:
        discount += 0.1
elif flowers_kind == 'Dahlias':
    price = 3.8
    if flowers_count > 90:
        discount += 0.15
elif flowers_kind == 'Tulips':
    price = 2.8
    if flowers_count > 80:
        discount += 0.15
elif flowers_kind == 'Narcissus':
    price = 3
    if flowers_count < 120:
        discount -= 0.15
elif flowers_kind == 'Gladiolus':
    price = 2.5
    if flowers_count < 80:
        discount -= 0.2

bill = flowers_count * price * (1 - discount)
difference = abs(budget - bill)

if budget >= bill:
    print(f'Hey, you have a great garden with {flowers_count} {flowers_kind} and {difference:.2f} leva left.')
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')