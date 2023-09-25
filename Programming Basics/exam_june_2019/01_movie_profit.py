"""
https://judge.softuni.org/Contests/Practice/Index/1699#1

Наети сте от "SoftUni Studios" да напишете програма която пресмята потенциалната печалба от продажбата на билети за филм.
Прожекцията на филма трае предварително зададен брой дни, като всеки ден се продават определен брой билети. Цената
на 1 билет се определя от студиото. За излъчване на продукцията, определен процент от общия приход остава за киното.

Вход
От конзолата се четат 5 реда:
1.	Име на филм - текст
2.	Брой дни - цяло число в диапазона [1… 90]
3.	Брой билети  - цяло число в диапазона [100… 100000]
4.	Цена на билет - реално число в диапазона [5.0… 25.0]
5.	Процент за киното - цяло число в диапазона [5... 35]

Изход
Да се отпечата на конзолата прихода от продажбите, в следния формат:
•	"The profit from the movie {име на филм} is {приход на студиото} lv."
Цената на прихода да бъде форматирана до втората цифра след десетичния знак.
"""

movie_name = input()
days_count = int(input())
tickets_count = int(input())
ticket_price = float(input())
percent_cinema_hall = float(input())

subtotal = ticket_price * tickets_count * days_count
hall_profit = subtotal * percent_cinema_hall / 100
studio_profit = subtotal - hall_profit

print(f'The profit from the movie {movie_name} is {studio_profit:.2f} lv.')