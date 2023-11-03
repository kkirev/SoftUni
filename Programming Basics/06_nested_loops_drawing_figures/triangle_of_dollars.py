# Да се напише програма, която чете число n, въведено от потребителя, и печата триъгълник от долари като в примерите:

n = int(input())

for row in range(1, n + 1):
    for col in range(row):
        print('$', end=' ')
    if row == n:
        break
    print()