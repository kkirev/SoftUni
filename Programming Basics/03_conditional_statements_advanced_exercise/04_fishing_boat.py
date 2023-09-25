budget = int(input())
season = input()
fisherman_count = int(input())

rent = 0
if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if fisherman_count <= 6:
    rent *= 0.9
elif 7 <= fisherman_count <= 11:
    rent *= 0.85
else:
    rent *= 0.75

if fisherman_count % 2 == 0:
    if season != 'Autumn':
        rent *= 0.95

difference = abs(budget - rent)

if budget >= rent:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')