"""
https://judge.softuni.org/Contests/Compete/Index/2414#6

Петър иска да купи N видеокарти, M процесора и P на брой рам памет. Ако броя на видеокартите е по-голям от този на
процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
•	Видеокарта – 250 лв./бр.
•	Процесор – 35% от цената на закупените видеокарти/бр.
•	Рам памет – 10% от цената на закупените видеокарти/бр.
Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.

Вход
Входът се състои от четири реда:
1.	Бюджетът на Петър - реално число в интервала [1.0…100000.0]
2.	Броят видеокарти - цяло число в интервала [1…100]
3.	Броят процесори - цяло число в интервала [1…100]
4.	Броят рам памет - цяло число в интервала [1…100]

Изход
На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
•	Ако бюджета е достатъчен:
"You have {остатъчен бюджет} leva left!"
•	Ако сумата надхвърля бюджета:
"Not enough money! You need {нужна сума} leva more!"
Резултатът да се форматира до втория знак след десетичната запетая.
"""

budget = float(input())
count_VC = int(input())
count_CPU = int(input())
count_RAM = int(input())

price_VC = 250
sum_VC = count_VC * price_VC
price_CPU = sum_VC * 0.35
price_RAM = sum_VC * 0.10

sum_needed = sum_VC + count_CPU * price_CPU + count_RAM * price_RAM

if count_VC > count_CPU:
    sum_needed *= 0.85

difference = abs(budget - sum_needed)

if sum_needed <= budget:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')