film_screening = input()
rows = int(input())
columns = int(input())

price = 0
hall_capacity = rows * columns

if film_screening == 'Premiere':
    price = 12
elif film_screening == 'Normal':
    price = 7.5
elif film_screening == 'Discount':
    price = 5

income = hall_capacity * price
print(f'{income:.2f}')
