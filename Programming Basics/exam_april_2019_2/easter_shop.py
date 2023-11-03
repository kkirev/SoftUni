"""
https://judge.softuni.org/Contests/Practice/Index/1637#7

Покрай великденските празници, квартален магазин започва да продава боядисани яйца.Вашата задача е да напишете програма,
 която да изчислява колко яйца са продадени, като знаете началната им бройка в магазина. По време на продажбата е
 възможно да бъдат доставени допълнителни бройки яйца. Ако в даден момент от изпълнението на програмата, клиент поиска
 да купи повече, отколкото има в наличност, или се получи команда "Close", програмата трябва да приключи изпълнение.

Вход
От конзолата се чете:
•	На първи ред - Началното количество яйца в магазина - цяло число в интервала [1… 10000]
•	След това поредица от два реда (до получаване на команда "Close" или при заявка за купуване на
повече от наличните в магазина яйца) :
    o	Команда за купуване или допълване на яйца в магазина – текст ("Buy" или "Fill")
    o	Брой на яйца, които да бъдат купени или допълнени в магазина – цяло число в интервала

[1… 1000]
Изход
На конзолата да се отпечатат два реда според случая:
•	При получаване на командата "Close":
    o	"Store is closed!"
    o	"{броя на продадените общо яйца} eggs sold."
•	При заявка за покупка на повече яйца, отколкото има в магазина:
    o	"Not enough eggs in store!"
    o	"You can buy only {броя на останалите в магазина яйца}."
"""

eggs_stock = int(input())
command = input()
sold_eggs = 0
shortage_eggs = False

while command != 'Close':
    transfer_eggs = command
    eggs_count = int(input())

    if transfer_eggs == 'Buy' and eggs_count > eggs_stock:
        shortage_eggs = True
        break
    if transfer_eggs == 'Fill':
        eggs_stock += eggs_count
    elif transfer_eggs == 'Buy':
        eggs_stock -= eggs_count
        sold_eggs += eggs_count

    command = input()

if command == 'Close':
    print(f'Store is closed!')
    print(f'{sold_eggs} eggs sold.')

if shortage_eggs:
    print(f'Not enough eggs in store!')
    print(f'You can buy only {eggs_stock}.')

# ----------------------------------------------------------------------------------------------------------------------
#
# eggs_stock = int(input())
# eggs_sold = 0
#
# while True:
#     shop_close = False
#     not_enough_eggs = False
#
#     command = input()
#     if command != "Close":
#         eggs_count = int(input())
#     else:
#         shop_close = True
#         break
#
#     if command == "Buy":
#         if eggs_count > eggs_stock:
#             not_enough_eggs = True
#             break
#         else:
#             eggs_stock -= eggs_count
#             eggs_sold += eggs_count
#     elif command == "Fill":
#         eggs_stock += eggs_count
#
# if shop_close:
#     print(f"Store is closed!")
#     print(f"{eggs_sold} eggs sold.")
# if not_enough_eggs:
#     print("Not enough eggs in store!")
#     print(f"You can buy only {eggs_stock}.")