"""
https://judge.softuni.org/Contests/Practice/Index/1637#4

По време на Великденските празници, Деси иска да отиде на почивка. В таблицата са показани кои са дестинациите и каква
е цената за нощувка спрямо датите, през които си е резервирала екскурзията.

Дестинация	        21-23 март	        24-27 март	        28-31 март
Франция	            30 лв.	            35 лв.	            40 лв.
Италия	            28 лв.	            32 лв.	            39 лв.
Германия	        32 лв.	            37 лв.	            43 лв.

Напишете програма, която изчислява колко ще струва екскурзията на Деси, като знаете дестинацията,
на която иска да отиде, кога си е резервирала екскурзията и за колко нощувки ще е в дадената страна.

Вход
Входът се чете от конзолата и се състои от три реда:
•	Първи ред - дестинация - текст с възможности"France", "Italy" или "Germany"
•	Втори ред - дати, през които си е резервирала екскурзията - текст  с възможности "21-23",
"24-27" или "28-31"
•	Трети ред - брой нощувки - цяло число в интервала [1… 100]

Изход
На конзолата трябва да се отпечата един ред:
"Easter trip to {дестинация} : {разходи за екскурзията} leva."
Разходите за екскурзията да бъдат форматирани до втората цифра след десетичния знак.
"""

destination = input()
trip_dates = input()
nights_count = int(input())

price_per_night = 0

if destination == 'France':
    if trip_dates == '21-23':
        price_per_night = 30
    elif trip_dates == '24-27':
        price_per_night = 35
    elif trip_dates == '28-31':
        price_per_night = 40

elif destination == 'Italy':
    if trip_dates == '21-23':
        price_per_night = 28
    elif trip_dates == '24-27':
        price_per_night = 32
    elif trip_dates == '28-31':
        price_per_night = 39

elif destination == 'Germany':
    if trip_dates == '21-23':
        price_per_night = 32
    elif trip_dates == '24-27':
        price_per_night = 37
    elif trip_dates == '28-31':
        price_per_night = 43

trip_expenses = nights_count * price_per_night

print(f'Easter trip to {destination} : {trip_expenses:.2f} leva.')