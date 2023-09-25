"""
https://judge.softuni.org/Contests/Practice/Index/1637#5

С наближаването на Великденските празници, цех за боядисване на яйца, започва да боядисва различни размери яйца,
които след това продава на партиди. В таблицата са показани размерите на яйцата, различните бои и каква е цената за
продажба на една партида яйца, зависеща от размерите и цвета боя.

	                    Червено (Red)	        Зелено (Green)	        Жълто (Yellow)
Големи (Large)	            16 лв.	                12 лв.	                9 лв.
Средни (Medium)	            13 лв.	                9 лв.	                7 лв.
Малки (Small)	            9 лв.	                8 лв.	                5 лв.

Напишете програма, която изчислява какви ще са приходите на цеха от продажбите, като знаете размера на яйцата и техният
цвят. С 35% от крайната цена ще бъдат покрити производствени разходи.

Вход
Входът се чете от конзолата и се състои от три реда:
•	Първи ред – размер на яйцата – текст с възможности "Large", "Medium" или "Small"
•	Втори ред – цвят на яйцата – текст  с възможности "Red", "Green" или "Yellow"
•	Трети ред – брой партиди – цяло число в интервала [1… 350]

Изход
На конзолата трябва да се отпечата един ред:
"{крайната цена} leva."
Резултатът да се форматира до втората цифра след десетичния знак.
Примерен вход и изход
"""

eggs_size = input()
eggs_color = input()
sets_count = int(input())

set_price = 0

if eggs_color == 'Red':
    if eggs_size == 'Large':
        set_price = 16
    elif eggs_size == 'Medium':
        set_price = 13
    elif eggs_size == 'Small':
        set_price = 9

elif eggs_color == 'Green':
    if eggs_size == 'Large':
        set_price = 12
    elif eggs_size == 'Medium':
        set_price = 9
    elif eggs_size == 'Small':
        set_price = 8

elif eggs_color == 'Yellow':
    if eggs_size == 'Large':
        set_price = 9
    elif eggs_size == 'Medium':
        set_price = 7
    elif eggs_size == 'Small':
        set_price = 5

factory_income = sets_count * set_price
factory_expenses = 0.35 * factory_income
factory_profit = factory_income - factory_expenses

print(f'{factory_profit:.2f} leva.')