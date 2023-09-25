# Напишете програма, която чете число n, въведено от потребителя, и чертае квадрат от n * n звездички.
# Разликата с предходната задача е, че между всеки две звездички има по един интервал.

stars_count = int(input())

for row in range(stars_count):
    for col in range(stars_count):
        print('*', end=' ')
    print()