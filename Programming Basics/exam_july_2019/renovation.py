# Пешо решава, че иска да направи ремонт вкъщи. Неговата задача е да боядиса стените в хола, като знаете височината и
# ширината на една стена. Холът на Пешо има 4 стени с еднакви размери, определен процент от които се заемат от прозорци
# и врати, които няма да бъдат боядисвани. Той не е сигурен дали ще успее наведнъж, затова моли Вас да му помогнете да
# изчисли дали ще му остава още работа за следващия ден и, ако да, колко кв. м. има да довърши,
# а в случай, че успее да боядиса хола, колко боя му е останала (трябва да се има предвид,
# че с един литър боя се боядисва един квадратен метър от стената).

# Вход
# От конзолата се четат следните редове:
# 1.	Височина на стената - цяло число [0… 100]
# 2.	Ширина на стената - цяло число [0… 100]
# 3.	Процент от общата площ на стените, който няма да бъде боядисан - цяло число [5… 95]
# На следващите редове до получаване на командата "Tired!" или докато не бъдат боядисани
# всички стени, се чете по едно число:
# •	Литри боя – цяло число [0…100]:
# Забележка: Площта за боядисване да бъде закръглена нагоре до най-близкото цяло число.

# Изход
# Да се отпечата на конзолата един от следните редове:
# •	При получаване на командата "Tired!":
# "{квадратни метри} quadratic m left."
# {квадратни метри} е повърхнината, която му остава да боядисана.
# •	Aко е останала боя в излишък:
# "All walls are painted and you have {литри боя} l paint left!"
# •	Aко след боядисването на всички стени, не е останала боя:
# "All walls are painted! Great job, Pesho!"

from math import ceil

wall_height = int(input())
wall_width = int(input())
percent_paintless_area = int(input())

walls_area = ceil(4 * wall_width * wall_height * ((100 - percent_paintless_area) / 100))
paint_litres_needed = walls_area
paint_litres_used = 0
is_done = False

command = input()
while command != 'Tired!':
    paint_litres = int(command)

    paint_litres_used += paint_litres
    paint_litres_needed -= paint_litres

    if paint_litres_needed <= 0:
        is_done = True
        break

    command = input()

if paint_litres_needed == paint_litres_used:
    print('All walls are painted! Great job, Pesho!')
elif paint_litres_needed < paint_litres_used:
    diff = abs(walls_area - paint_litres_used)
    print(f'All walls are painted and you have {diff} l paint left!')
else:
    diff = abs(walls_area - paint_litres_used)
    print(f'{diff} quadratic m left.')