"""
https://judge.softuni.org/Contests/Practice/Index/1680#0

Напишете програма, която да пресмята резултата от игра. Първо получавате число, което показва колко хода ще продължи
играта. После за всеки ход на играта ще получавате по едно ново число. Според интервала в който попада числото се
прибавят точки. Ако числото е отрицателно или по-голямо 50, тогава то е невалидно. В началото на играта
резултата е 0 и на всеки ход се прибавят точки по следният начин:
•	От 0  до  9  20 % от числото
•	От 10 до 19  30 % от числото
•	От 20 до 29  40 % от числото
•	От 30 до 39  50 точки
•	От 40 до 50  100 точки
•	Невалидно число  резултата се дели на 2

Освен резултата програмата трябва да изкарва статистика за проценти числа в дадените интервали.

Вход
Входът се чете от конзолата:
•	Първи ред - колко хода ще има по време на играта – цяло число в интервала [1...100]
•	За всеки ход – числата, които се проверяват в кой интервал са – цели числа в интервала [-100...100]

Изход
Да се отпечата на конзолата 7 реда:
•	1ви ред: "{Краен резултат}"
•	2ри ред: "From 0 to 9: {процент в интервала}%"
•	3ти ред: "From 10 to 19: {процент в интервала}%"
•	4ти ред: "From 20 to 29: {процент в интервала}%"
•	5ти ред: "From 30 to 39: {процент в интервала}%"
•	6ти ред: "From 40 to 50: {процент в интервала}%"
•	7ми ред: "Invalid numbers: {процент в интервала}%"
Всички числа трябва да са форматирана до вторият знак след запетаята.
"""
# User input
turns_count = int(input())

# Logic
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid = 0
result = 0

for turn in range(1, turns_count + 1):
    number = int(input())
    if 0 <= number < 10:
        from_0_to_9 += 1
        result += number * 0.20
    elif 10 <= number < 20:
        from_10_to_19 += 1
        result += number * 0.30
    elif 20 <= number < 30:
        from_20_to_29 += 1
        result += number * 0.40
    elif 30 <= number < 40:
        from_30_to_39 += 1
        result += 50
    elif 40 <= number <= 50:
        from_40_to_50 += 1
        result += 100
    elif number < 0 or number > 50:
        invalid += 1
        result /= 2

# Output
print(f'{result:.2f}')
print(f'From 0 to 9: {from_0_to_9 / turns_count * 100:.2f}%')
print(f'From 10 to 19: {from_10_to_19 / turns_count * 100:.2f}%')
print(f'From 20 to 29: {from_20_to_29 / turns_count * 100:.2f}%')
print(f'From 30 to 39: {from_30_to_39 / turns_count * 100:.2f}%')
print(f'From 40 to 50: {from_40_to_50 / turns_count * 100:.2f}%')
print(f'Invalid numbers: {invalid / turns_count * 100:.2f}%')