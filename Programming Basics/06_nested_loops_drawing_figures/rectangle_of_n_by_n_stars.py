# Напишете програма, която чете цяло положително число n, въведено от потребителя
# и печата на конзолата правоъгълник от n * n звездички.

stars_count = int(input())

for row in range(stars_count):
    for col in range(stars_count):
        print('*', end='')
    print()