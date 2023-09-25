"""
https://judge.softuni.org/Contests/Practice/Index/1699#3

За предстояща премиера на три известни продукции, местно кино ви наема да напишете софтуер, който да изчислява цената,
която клиентите трябва да заплатят, според филма и пакета, който са избрали.

	        John Wick	        Star Wars	        Jumanji
Напитка	    12 лв./бр.	        18 лв. /бр.	        9 лв. /бр.
Пуканки	    15 лв. /бр.	        25 лв. /бр.	        11 лв. /бр.
Меню	    19 лв. /бр.	        30 лв. /бр.	        14 лв. /бр.

Напишете програма, която изчислява цената, която трябва да се заплати, като имате в предвид следните отстъпки:
•	При избран филм "Star Wars" и закупени поне четири билета, има 30% семейна отстъпка.
•	При избран филм "Jumanji" и закупени точно два билета, има 15% отстъпка за двама.

Вход
Входът се чете от конзолата и се състои от три реда:
•	Първи ред - прожекция - текст с възможности"John Wick", "Star Wars" или "Jumanji"
•	Втори ред - пакет за филм - текст  с възможности "Drink", "Popcorn" или "Menu"
•	Трети ред - брой билети - цяло число в интервала [1… 30]

Изход
На конзолата трябва да се отпечата един ред:
"Your bill is {крайна цена} leva."
Цената да бъде закръглена до втората цифра след десетичния знак.
"""

movie_name = input()
ticket_addition = input()
tickets_count = int(input())

ticket_price = 0

if movie_name == 'John Wick':
    if ticket_addition == 'Drink':
        ticket_price = 12
    elif ticket_addition == 'Popcorn':
        ticket_price = 15
    elif ticket_addition == 'Menu':
        ticket_price = 19

elif movie_name == 'Star Wars':
    if ticket_addition == 'Drink':
        ticket_price = 18
    elif ticket_addition == 'Popcorn':
        ticket_price = 25
    elif ticket_addition == 'Menu':
        ticket_price = 30

elif movie_name == 'Jumanji':
    if ticket_addition == 'Drink':
        ticket_price = 9
    elif ticket_addition == 'Popcorn':
        ticket_price = 11
    elif ticket_addition == 'Menu':
        ticket_price = 14

total_sum = ticket_price * tickets_count

if movie_name == 'Star Wars' and tickets_count >= 4:
    total_sum *= 0.7
elif movie_name == 'Jumanji' and tickets_count == 2:
    total_sum *= 0.85

print(f'Your bill is {total_sum:.2f} leva.')