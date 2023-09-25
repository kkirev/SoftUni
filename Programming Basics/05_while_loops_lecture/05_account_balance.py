# Напишете програма, която пресмята колко общо пари има в сметката, след като направите определен брой вноски.
# На всеки ред ще получавате сумата, която трябва да внесете в сметката, до получаване на команда  "NoMoreMoney ".
# При всяка получена сума на конзолата трябва да се извежда "Increase: " + сумата и тя да се прибавя в сметката.
# Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!"  и програмата да приключи.
# Когато програмата приключи трябва да се принтира "Total: " + общата сума в сметката форматирана
# до втория знак след десетичната запетая.

total_sum = 0
command = input()

while command != 'NoMoreMoney':
    current_sum = float(command)
    if current_sum < 0:
        print(f'Invalid operation!')
        break
    print(f'Increase: {current_sum:.2f}')
    total_sum += current_sum
    command = input()
print(f'Total: {total_sum:.2f}')