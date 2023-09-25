"""
https://judge.softuni.org/Contests/Practice/Index/2275#8

Ани намира кученце, за което ще се грижи, докато се намери някой да го осинови. То изяжда дневно определено количество
храна. Да се напише програма, която проверява дали количеството храна, което е закупено за кученцето,
ще е достатъчно докато кученцето бъде осиновено.

Вход
От конзолата се прочитат:
•	Закупеното количество храна за кученцето в килограми – цяло число в интервала [1 …100]
•	На всеки следващ ред до получаване на команда Adopted ще получавате колко грама изяжда кученцето на
всяко хранене - цяло число в интервала [10 …1000]

Изход
На конзолата се отпечатва 1 ред:
•	Ако количеството храна е достатъчно да се отпечата:
 	"Food is enough! Leftovers: {останала храна} grams."
•	Ако количеството храна не е достатъчно да се отпечата:
 	"Food is not enough. You need {нужно количество храна} grams more."
"""

total_food_kg = int(input())
user_input = input()

total_food_gr = total_food_kg * 1000
total_eaten_food = 0

while user_input != 'Adopted':
    food_eaten = float(user_input)
    total_eaten_food += food_eaten
    if user_input == 'Adopted':
        break
    user_input = input()

difference = abs(total_eaten_food - total_food_gr)

if total_food_gr >= total_eaten_food:
    print(f'Food is enough! Leftovers: {difference:.0f} grams.')
else:
    print(f'Food is not enough. You need {difference:.0f} grams more.')