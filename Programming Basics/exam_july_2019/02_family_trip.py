# Семейство Иванови планират семейната си почивка. Вашата задача е да напишете програма, която да изчислява дали
# предвидения от тях бюджет ще им стигне, като знаете колко нощувки са планирали, каква е цената за нощувка и колко
# процента от бюджета са предвидили за допълнителни разходи. Трябва да се има предвид, че ако броят на
# нощувките е по-голям от 7, цената за нощувка се намаля с 5%.

# Вход
# От конзолата се четат 4 реда:
# •	Бюджетът, с който разполагат – реално число в интервала [1.00 … 10000.00]
# •	Брой нощувки – цяло число в интервала [0 … 1000]
# •	Цена за нощувка – реално число в интервала [1.00 … 500.00]
# •	Процент за допълнителни разходи – цяло число в интервала [0 … 100]

# Изход
# Отпечатването на конзолата зависи от резултата:
# •	Ако сумата е достатъчна:
# o	"Ivanovi will be left with {останали пари след почивката} leva after vacation."
# •	Ако НЕ е достигната сумата:
# o	"{парите нужни до достигане на целта} leva needed."
# Сума трябва да се форматира до втората цифра след десетичния знак.

budget = float(input())
nights_count = int(input())
price_per_nights = float(input())
additional_percent = int(input()) / 100

additional_expenses = budget * additional_percent

if nights_count > 7:
    price_per_nights *= 0.95
else: price_per_nights = price_per_nights

money_left_over = budget - (nights_count * price_per_nights + additional_expenses)
money_needed = (nights_count * price_per_nights + additional_expenses) - budget

if budget >= nights_count * price_per_nights + additional_expenses:
    print(f"Ivanovi will be left with {money_left_over:.2f} leva after vacation.")
else: print(f"{money_needed:.2f} leva needed.")