"""
https://judge.softuni.org/Contests/Practice/Index/1637#8

Предстои Великден и едно от най-вълнуващите неща е боядисването на яйца. Наличните цветове за боядисване са:
•	червено (red)
•	оранжев (orange)
•	син (blue)
•	зелен (green)
Напишете програма, която изчислява какъв е броят на яйцата от всеки цвят и от кой цвят яйцата са най - много,
като знаете общия им брой и цвета на всяко яйце.

Вход
От конзолата се чете 1 ред:
•	 Броят на боядисаните яйца – цяло число в интервала [1 ... 100]
За всяко яйце се чете:
    o	Цветът на яйцето – текст с възможности: "red", "orange", "blue", "green"

Изход
Да се отпечатат на конзолата 5 реда:
•	"Red eggs: {брой на червените яйца}"
•	"Orange eggs: {брой на оранжевите яйца}"
•	"Blue eggs: {брой на сините яйца}"
•	"Green eggs: {брой на зелените яйца}"
•	"Max eggs: {максимален брой на яйцата от цвят} -> {цвят}"
"""

eggs_count = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
most_eggs = 0
most_color = ''

for egg in range(eggs_count):
    egg_color = input()

    if egg_color == 'red':
        red_eggs += 1
    elif egg_color == 'orange':
        orange_eggs += 1
    elif egg_color == 'blue':
        blue_eggs += 1
    elif egg_color == 'green':
        green_eggs += 1

    if red_eggs > orange_eggs and red_eggs > blue_eggs and red_eggs > green_eggs:
        most_color = 'red'
        most_eggs = red_eggs
    elif orange_eggs > red_eggs and orange_eggs > blue_eggs and orange_eggs > green_eggs:
        most_color = 'orange'
        most_eggs = orange_eggs
    elif blue_eggs > red_eggs and blue_eggs > orange_eggs and blue_eggs > green_eggs:
        most_color = 'blue'
        most_eggs = blue_eggs
    elif green_eggs > red_eggs and green_eggs > orange_eggs and green_eggs > blue_eggs:
        most_color = 'green'
        most_eggs = green_eggs

print(f'Red eggs: {red_eggs}')
print(f'Orange eggs: {orange_eggs}')
print(f'Blue eggs: {blue_eggs}')
print(f'Green eggs: {green_eggs}')
print(f'Max eggs: {most_eggs} -> {most_color}')

# ----------------------------------------------------------------------------------------------------------------------
#
# painted_eggs_count = int(input())
# red_eggs = 0
# orange_eggs = 0
# blue_eggs = 0
# green_eggs = 0
# total_eggs = red_eggs + orange_eggs + blue_eggs + green_eggs
# max_eggs_count = 0
# max_eggs_color = ''
#
# for egg in range(painted_eggs_count):
#     color = input()
#
#     if color == "red":
#         red_eggs += 1
#         if red_eggs > max_eggs_count:
#             max_eggs_count = red_eggs
#             max_eggs_color = "red"
#
#     elif color == "orange":
#         orange_eggs += 1
#         if orange_eggs > max_eggs_count:
#             max_eggs_count = orange_eggs
#             max_eggs_color = "orange"
#
#     elif color == "blue":
#         blue_eggs += 1
#         if blue_eggs > max_eggs_count:
#             max_eggs_count = blue_eggs
#             max_eggs_color = "blue"
#
#     elif color == "green":
#         green_eggs += 1
#         if green_eggs > max_eggs_count:
#             max_eggs_count = green_eggs
#             max_eggs_color = "green"
#
# print(f"Red eggs: {red_eggs}")
# print(f"Orange eggs: {orange_eggs}")
# print(f"Blue eggs: {blue_eggs}")
# print(f"Green eggs: {green_eggs}")
# print(f"Max eggs: {max_eggs_count} -> {max_eggs_color}")
