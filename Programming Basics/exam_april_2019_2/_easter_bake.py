"""
https://judge.softuni.org/Contests/Practice/Index/1637#9

Предстои Великден и Деси е решила да изпече домашни козунаци за колегите си. Главните продукти, които ще трябват на
Деси са: брашно и захар. Един пакет захар е 950 грама, а един пакет брашно е 750 грама. Напишете програма, която
изчислява колко пакета захар и брашно трябва да купи Деси, за да й стигнат за направата на козунаците, като знаете за
всеки един козунак по колко грама захар и брашно са изразходени.
Също намерете кое е най-голямото количество захар и брашно, които са използвани.

Вход
От конзолата се чете 1 ред:
•	 Броят на козунаците – цяло число в интервала [1 ... 100]
За всеки козунак се чете:
    o	Количество изразходвана захар (грамове) – цяло число в интервала [1 … 10000]
    o	Количество изразходвано брашно (грамове) – цяло число в интервала [1 … 10000]

Изход
Да се отпечатат на конзолата 3 реда:
•	"Sugar: {брой нужни пакети захар}"
•	"Flour: {брой нужни пакет брашно}"
•	"Max used flour is {максимално количество грамове брашно, използвани за правенето на козунак} grams,
max used sugar is {максимално количество грамове захар, използвани за правенето на козунак} grams."
Пакетите захар и брашно да бъдат закръглени към най-близкото цяло число нагоре.
"""

from math import ceil

easter_breads_count = int(input())

sugar_grams = 0
flour_grams = 0
max_sugar_added = 0
max_flour_added = 0

for bread in range(easter_breads_count):
    sugar_cost = int(input())
    flour_cost = int(input())

    sugar_grams += sugar_cost
    flour_grams += flour_cost

    if sugar_cost > max_sugar_added:
        max_sugar_added = sugar_cost

    if flour_cost > max_flour_added:
        max_flour_added = flour_cost

    sugar_packs = sugar_grams / 950
    flour_packs = flour_grams / 750

print(f'Sugar: {ceil(sugar_packs)}')
print(f'Flour: {ceil(flour_packs)}')
print(f'Max used flour is {max_flour_added} grams, max used sugar is {max_sugar_added} grams.')