"""
https://judge.softuni.org/Contests/Compete/Index/2424#7

Джеси решава, че иска да се занимава с баскетбол, но за да тренира е нужна екипировка.
Напишете програма, която изчислява какви разходи ще има Джеси, ако започне да тренира, като знаете колко е таксата за
тренировки по баскетбол за период от 1 година. Нужна екипировка:
•	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
•	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
•	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
•	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

Вход
От конзолата се четe 1 ред:
•	Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]

Изход
Да се отпечата на конзолата колко ще са разходите на Джеси, ако започне да спортува баскетбол.
"""
annual_fee = int(input())

sneakers = annual_fee - annual_fee * 0.4
clothes = sneakers - sneakers * 0.2
ball = clothes / 4
accessories = ball / 5

total_sum = sneakers + clothes + ball + accessories

print(f'{(total_sum + annual_fee):.2f}')