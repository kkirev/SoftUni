"""
https://judge.softuni.org/Contests/Practice/Index/1637#11

За великденските празници, магазин започва да продава три вида великденска украса – кошнички за яйца (basket),
великденски венци (wreath) и шоколадови зайци (chocolate bunny). Вашата задача е да напишете програма, която да
изчислява каква сметка трябва да плати всеки един клиент на магазина, като се има в предвид,
че всеки клиент закупил четен брой продукти, ще получи 20% отстъпка от крайната цена.
След като всички клиенти приключат с покупките, трябва да се отпечата средно по колко пари е похарчил всеки човек.
Цените на продуктите са:
•	кошничка за яйца (basket) – 1.50 лв.
•	великденски венец (wreath) – 3.80 лв.
•	шоколадов заек (chocolate bunny) – 7 лв.

Вход
От конзолата първоначално се чете един ред:
•	Брои на клиентите в магазина – цяло число [1… 100]
•	След това за всеки един клиент на нов ред до получаване на командата "Finish" се чете:
    o	Покупката която клиента е избрал – текст ("basket", "wreath" или "chocolate bunny")

Изход
•	При получаване на командата "Finish" да се отпечата един ред:
    o	"You purchased {броя на покупките} items for {крайната цена} leva."
•	Накрая, след като всички клиенти приключат с покупките, да се отпечата на един ред
    o	"Average bill per client is: {средно аритметично на парите които е похарчил всеки един клиент} leva."
Всички пари трябва да бъдат форматирани до втората цифра след десетичния знак.
"""

client_items = 0
total_items = 0
client_bill = 0
total_bills = 0

clients_count = int(input())
for client in range(clients_count):
    command = input()

    client_bill = 0
    client_items = 0

    while command != 'Finish':
        item = command
        client_items += 1
        total_items += 1

        if item == 'basket':
            client_bill += 1.5
        elif item == 'wreath':
            client_bill += 3.8
        elif item == 'chocolate bunny':
            client_bill += 7

        command = input()

        if command == 'Finish':
            if client_items % 2 == 0:
                client_bill *= 0.8
            total_bills += client_bill
            print(f'You purchased {client_items} items for {client_bill:.2f} leva.')

average_bill = total_bills / clients_count

print(f'Average bill per client is: {average_bill:.2f} leva.')

# ----------------------------------------------------------------------------------------------------------------------
#
# customers_count = int(input())
# total_sum = 0
#
# for customer in range(customers_count):
#     items_count = 0
#     current_bill = 0
#     command = input()
#     while command != "Finish":
#         purchase = command
#         items_count += 1
#
#         if purchase == "basket":
#             current_bill += 1.5
#         elif purchase == "wreath":
#             current_bill += 3.8
#         elif purchase == "chocolate bunny":
#             current_bill += 7
#
#         command = input()
#
#         if command == "Finish":
#             if items_count % 2 == 0:
#                 current_bill *= 0.8
#             total_sum += current_bill
#             print(f"You purchased {items_count} items for {current_bill:.2f} leva.")
# average_bill = total_sum / customers_count
# print(f"Average bill per client is: {average_bill:.2f} leva.")