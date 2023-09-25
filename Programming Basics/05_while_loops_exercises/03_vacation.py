"""
https://judge.softuni.org/Contests/Compete/Index/2420#1

Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да
събере необходимата сума. Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи повече от наличните
си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.

Вход
От конзолата се четат:
•	Пари, нужни за екскурзията - реално число;
•	Налични пари - реално число.
След това многократно се четат по два реда:
•	Вид действие – текст с две възможности: "spend" или "save";
•	Сумата, която ще спести/похарчи - реално число.

Изход
Програмата трябва да приключи при следните случаи:
•	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
o	"You can't save the money."
o	"{Общ брой изминали дни}"
•	Ако Джеси събере парите за почивката, на конзолата се изписва:
o	"You saved the money for {общ брой изминали дни} days."
"""

money_needed = float(input())
money_owned = float(input())

spent_counter = 0
days = 0

while money_owned <= money_needed or spent_counter == 5:
    if spent_counter == 5:
        break
    if money_owned >= money_needed:
        break
    days += 1
    action_type = input()
    current_money = float(input())
    if action_type == 'spend':
        money_owned -= current_money
        if money_owned < 0:
            money_owned = 0
        spent_counter += 1
    elif action_type == 'save':
        spent_counter = 0
        money_owned += current_money

if spent_counter == 5:
    print("You can't save the money.")
    print(f'{days}')
if money_owned >= money_needed:
    print(f'You saved the money for {days} days.')

#---------------------------------------------------------------------
#
# money_needed = float(input())
# money_owned = float(input())
#
# spent_counter = 0
# days = 0
#
# while True:
#     action_type = input()
#     current_money = float(input())
#     days += 1
#
#     if action_type == 'spend':
#         spent_counter += 1
#         money_owned -= current_money
#         if money_owned < 0:
#             money_owned = 0
#     elif action_type == 'save':
#         spent_counter = 0
#         money_owned += current_money
#
#     if money_owned >= money_needed:
#         print(f'You saved the money for {days} days.')
#         break
#     elif spent_counter == 5:
#         print("You can't save the money.")
#         print(f'{days}')
#         break