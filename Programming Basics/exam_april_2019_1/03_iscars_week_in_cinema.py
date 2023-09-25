"""
По време на седмицата на Оскарите, градското кино пуска прожекции на някои от филмите, които са номинирани в
категорията за "Най-добър филм". В таблицата са показани кои са филмите и каква е цената за прожекция спрямо залата,
в която се прожектира филмът.
Филм	                normal	    luxury	    ultra luxury
A Star Is Born	    7.50 лв.	10.50 лв.	13.50 лв.
Bohemian Rhapsody	    7.35 лв.	9.45 лв.	12.75 лв.
Green Book	        8.15 лв.	10.25 лв.	13.25 лв.
The Favourite	        8.75 лв.	11.55 лв.	13.95 лв.
Напишете програма, която изчислява какъв е приходът от даден филм, като знаете в какъв тип зала се прожектира и
колко човека са си купили билет за прожекцията.

Вход
Входът се чете от конзолата и се състои от три реда:
•	Първи ред – име на филм – текст ("A Star Is Born", "Bohemian Rhapsody","Green Book" или "The Favourite")
•	Втори ред– вид на залата – текст ("normal", "luxury" или "ultra luxury")
•	Трети ред – брой на закупените билети – цяло число в интервала [1…100]

Изход
На конзолата трябва да се отпечата един ред:
"{име на филма} -> {приходи от прожекцията на филма} lv."
Приходите да бъдат закръглени до втория знак след десетичната запетая.
"""

movie = input()
hall_category = input()
tickets_count = int(input())

ticket_price = 0
if movie == 'A Star Is Born':
    if hall_category == 'normal':
        ticket_price = 7.5
    elif hall_category == 'luxury':
        ticket_price = 10.5
    elif hall_category == 'ultra luxury':
        ticket_price = 13.5
elif movie == 'Bohemian Rhapsody':
    if hall_category == 'normal':
        ticket_price = 7.35
    elif hall_category == 'luxury':
        ticket_price = 9.45
    elif hall_category == 'ultra luxury':
        ticket_price = 12.75
elif movie == 'Green Book':
    if hall_category == 'normal':
        ticket_price = 8.15
    elif hall_category == 'luxury':
        ticket_price = 10.25
    elif hall_category == 'ultra luxury':
        ticket_price = 13.25
elif movie == 'The Favourite':
    if hall_category == 'normal':
        ticket_price = 8.75
    elif hall_category == 'luxury':
        ticket_price = 11.55
    elif hall_category == 'ultra luxury':
        ticket_price = 13.95

income = tickets_count * ticket_price

print(f'{movie} -> {income:.2f} lv.')