month = input()
nights_count = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if 7 < nights_count <= 14:
        studio_price *= 0.95
    elif nights_count > 14:
        studio_price *= 0.7
        apartment_price *= 0.9
if month == 'June' or month == 'September':
    studio_price = 75.2
    apartment_price = 68.7
    if nights_count > 14:
        studio_price *= 0.8
        apartment_price *= 0.9
if month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77
    if nights_count > 14:
        apartment_price *= 0.9

print(f'Apartment: {nights_count * apartment_price:.2f} lv.')
print(f'Studio: {nights_count * studio_price:.2f} lv.')