"""
https://judge.softuni.org/Contests/2418

Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване.
Според размера на групата, катерачите ще изкачват различни върхове.
•	Група до 5 човека – изкачват Мусала
•	Група от 6 до 12 човека – изкачват Монблан
•	Група от 13 до 25 човека – изкачват Килиманджаро
•	Група от 26 до 40 човека –  изкачват К2
•	Група от 41 или повече човека – изкачват Еверест
Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.

Вход
От конзолата се четат поредица от числа, всяко на отделен ред:
•	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
•	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]

Изход
Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с точност до
втората цифра след десетичната запетая.
•	Първи ред - процентът изкачващи Мусала
•	Втори ред – процентът изкачващи Монблан
•	Трети ред – процентът изкачващи Килиманджаро
•	Четвърти ред – процентът изкачващи К2
•	Пети ред – процентът изкачващи Еверест
"""
groups_count = int(input())

chosed_musala = 0
chosed_monblan = 0
chosed_kilimanjaro = 0
chosed_k2 = 0
chosed_everest = 0
total_climbers = 0

for _ in range(groups_count):
    climbers_count = int(input())
    total_climbers += climbers_count
    if climbers_count <= 5:
        chosed_musala += climbers_count
    elif 5 < climbers_count <= 12:
        chosed_monblan += climbers_count
    elif 12 < climbers_count <= 25:
        chosed_kilimanjaro += climbers_count
    elif 25 < climbers_count <= 40:
        chosed_k2 += climbers_count
    elif climbers_count > 40:
        chosed_everest += climbers_count

percent_climbed_musala = chosed_musala / total_climbers * 100
percent_climbed_monblan = chosed_monblan / total_climbers * 100
percent_climbed_kilimanjaro = chosed_kilimanjaro / total_climbers * 100
percent_climbed_k2 = chosed_k2 / total_climbers * 100
percent_climbed_everest = chosed_everest / total_climbers * 100

print(f'{percent_climbed_musala:.2f}%')
print(f'{percent_climbed_monblan:.2f}%')
print(f'{percent_climbed_kilimanjaro:.2f}%')
print(f'{percent_climbed_k2:.2f}%')
print(f'{percent_climbed_everest:.2f}%')
