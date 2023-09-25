# Напишете програма, която чете цяло число n, въведено от потребителя, и отпечатва пирамида от числа като в примерите:

number = int(input())
curr_num = 1
is_finished = False

for row in range(1, number + 1):
    for col in range(1, row + 1):
        if curr_num > number:
            is_finished = True
            break
        print(curr_num, end= ' ')
        curr_num += 1

    if is_finished:
        break
    print()