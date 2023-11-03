"""
https://judge.softuni.org/Contests/Practice/Index/1654#3

Времето се затопля и туристи, започват да си правят разходки високо в планината, където все още сняг, като за целта те
трябва да закупят нужната туристическа екипировка. Вашата задача е да напишете програма, която да изчислява, стойността
на екипировката, както и дали определения бюджет е достатъчен или не, като се знае, че в магазина има следната промоция:
Всеки трети продукт е на половин цена.

Вход
От конзолата се чете:
•	На първи ред – бюджетът - реално число в интервала [1.00… 100000.00]
•	След това поредица от два реда (до получаване на команда "Stop" или при заявка за купуване на продукт,
чиято стойност е по-висока от наличния бюджет) :
    o	Име на продукта – текст
    o	Цена на продукта – реално число в интервала [1.00… 5000.00]

Изход
На конзолата да се отпечатат следните редове според случая:
•	При получаване на командата "Stop", на един ред:
o	"You bought {брой на закупените продукти} products for {цена на покупките} leva."
•	При заявка за покупка на продукт, чиято цена е по-висока от останалите пари, на два реда:
    o	"You don't have enough money!"
    o	"You need {недостигащи пари} leva!"
"""

budget = float(input())
command = input()
total_sum = 0
items_count = 0
out_of_money = False

while command != 'Stop':
    item_name = command
    item_price = float(input())
    items_count += 1

    if items_count % 3 == 0:
        item_price /= 2

    if budget < item_price:
        out_of_money = True
        break

    total_sum += item_price
    budget -= item_price

    command = input()

diff = abs(budget - item_price)

if out_of_money:
    print(f"You don't have enough money!")
    print(f'You need {diff:.2f} leva!')
else:
    print(f'You bought {items_count} products for {total_sum:.2f} leva.')