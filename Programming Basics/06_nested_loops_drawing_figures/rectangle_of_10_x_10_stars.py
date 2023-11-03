# Напишете програма, която чертае на конзолата правоъгълник от 10 x 10 звездички.

for row in range(10):
    for col in range(10):
        print('*', end='')
    print()