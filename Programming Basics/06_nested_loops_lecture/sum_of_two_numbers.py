# Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа.
# На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число.
# Ако няма нито една комбинация отговаряща на условието се отпечатва съобщение, че не е намерено.

# Вход
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред – начало на интервала – цяло число в интервала [1...999]
# •	Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
# •	Трети ред – магическото число – цяло число в интервала [1...10000]

# Изход
# На конзолата трябва да се отпечата един ред, според резултата:
# •	Ако е намерена комбинация чиито сбор на числата е равен на магическото число
# o	"Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
# •	Ако не е намерена комбинация отговаряща на условието
# o	"{броят на всички комбинации} combinations - neither equals {магическото число}"

start_num = int(input())
end_num = int(input())
magic_num = int(input())

combinations_counter = 0
combinations_found = False

for first_num in range(start_num, end_num + 1):
    for second_num in range(start_num, end_num + 1):
        combinations_counter += 1
        if first_num + second_num == magic_num:
            combinations_found = True
            break
    if combinations_found:
        break

if combinations_found:
    print(f'Combination N:{combinations_counter} ({first_num} + {second_num} = {magic_num})')
else:
    print(f'{combinations_counter} combinations - neither equals {magic_num}')
