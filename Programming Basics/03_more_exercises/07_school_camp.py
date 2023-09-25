season = input()
students_gender = input()
students_count = int(input())
nights_count = int(input())

night_price = 0
sport = ''

if season == 'Winter':
    if students_gender == 'boys' or students_gender == 'girls':
        night_price = 9.6
    elif students_gender == 'mixed':
        night_price = 10
elif season == 'Spring':
    if students_gender == 'boys' or students_gender == 'girls':
        night_price = 7.2
    elif students_gender == 'mixed':
        night_price = 9.5
elif season == 'Summer':
    if students_gender == 'boys' or students_gender == 'girls':
        night_price = 15
    elif students_gender == 'mixed':
        night_price = 20

if season == 'Winter' and students_gender == 'girls':
    sport = 'Gymnastics'
elif season == 'Winter' and students_gender == 'boys':
    sport = 'Judo'
elif season == 'Winter' and students_gender == 'mixed':
    sport = 'Ski'
elif season == 'Spring' and students_gender == 'girls':
    sport = 'Athletics'
elif season == 'Spring' and students_gender == 'boys':
    sport = 'Tennis'
elif season == 'Spring' and students_gender == 'mixed':
    sport = 'Cycling'
elif season == 'Summer' and students_gender == 'girls':
    sport = 'Volleyball'
elif season == 'Summer' and students_gender == 'boys':
    sport = 'Football'
elif season == 'Summer' and students_gender == 'mixed':
    sport = 'Swimming'

price = students_count * nights_count * night_price

if students_count >= 50:
    price *= 0.5
elif 20 <= students_count < 50:
    price *= 0.85
elif 10 <= students_count < 20:
    price *= 0.95

print(f'{sport} {price:.2f} lv.')