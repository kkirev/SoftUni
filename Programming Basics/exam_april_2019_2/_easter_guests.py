"""
https://judge.softuni.org/Contests/Practice/Index/1637#3

Любо очаква гости за Великден.Той разполага с определен бюджет, който е предвидил, за да купи козунаци и боядисани яйца.
Известно е, че един козунак стига за трима човека, като всеки гост ще получи и по 2 яйца. Вашата задача е да намерите
колко козунака и яйца трябва да купи Любо, както и каква ще е сумата, която той трябва да плати и дали бюджета му е
достатъчен. При изчисляването на броя козунаци, които Любо трябва да закупи, техният брой трябва да се закръгли към
по-голямото цяло число.  Ако парите не му стигат, трябва да се изведе съобщение, колко не му достигат.
Известно е, че:
•	Един козунак струва 4лв.
•	Едно яйце струва 0.45лв.

Вход
От конзолата се четат 2 реда:
•	На първия ред са броят на гостите – цяло число в интервала [0 ... 200000]
•	На втория ред е бюджетът с който разполага Любо  – цяло число в интервала [0 ... 200000]

Изход
На конзолата да се отпечатат два реда:
•	Ако бюджетът е достатъчен:
    o	"Lyubo bought {брои закупени козунаци} Easter bread and {брои закупени яйца} eggs."
    o	"He has {останали пари} lv. left."
•	Ако  бюджетът НЕ Е достатъчен:
    o	"Lyubo doesn't have enough money."
    o	"He needs {недостигащи пари} lv. more."
Парите да бъдат форматирани до втората цифра след десетичния знак.
"""

import math
from math import ceil

guests_number = int(input())
budget = float(input())

easter_bread_pcs = math.ceil(guests_number / 3)
easter_eggs_pcs = guests_number * 2

sum_needed = easter_bread_pcs * 4 + easter_eggs_pcs * 0.45
diff = abs(budget - sum_needed)

if budget >= sum_needed:
    print(f'Lyubo bought {easter_bread_pcs} Easter bread and {easter_eggs_pcs} eggs.')
    print(f'He has {diff:.2f} lv. left.')
else:
    print(f"Lyubo doesn't have enough money.")
    print(f'He needs {diff:.2f} lv. more.')