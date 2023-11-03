budget = float(input())
season = input()

destination = ''
accommodation = ''
expenses = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        expenses = budget * 0.3
        accommodation = 'Camp'
    elif season == 'winter':
        accommodation = 'Hotel'
        expenses = budget * 0.7
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        expenses = budget * 0.4
        accommodation = 'Camp'
    elif season == 'winter':
        accommodation = 'Hotel'
        expenses = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    expenses = budget * 0.9
    accommodation = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{accommodation} - {expenses:.2f}')
