"""
https://judge.softuni.org/Contests/Practice/Index/1699#7

От телевизионна компания ви наемат да създадете програма, която да изчислява дали за клиентите ще е възможно да си
закупят желаните сериали. Разполагате с бюджет и брой сериали, които потребителят ще желае да закупи.
Всеки сериал съответно има заглавие и цена.
Някои от сериалите имат намаление:

•	Thrones     – 50%
•	Lucifer     – 40%
•	Protector   – 30%
•	TotalDrama  – 20%
•	Area        – 10%

Вход
От конзолата се четат:
•	Бюджет  - реално  число в интервала [10.0… 100.0]
•	Брой сериали - n - цяло положително число в интервала [1… 10]
За всеки сериал се четат по два реда:
o	Име на сериал - текст
o	Цена за сериал -  реално  число в интервала [1.0… 15.0]

Изход
На конзолата да се изпише един ред:
•	Ако бюджета ви е по-голям или равен на цената на сериалите:
	"You bought all the series and left with {останали пари} lv."
•	Ако бюджета ви е по-малък от цената на сериалите:
	"You need {нужни пари} lv. more to buy the series!"
Резултатът да бъде закръглен до втората цифра след десетичния знак.
"""

budget = float(input())
series_count = int(input())
final_price = 0
total_sum = 0

for series in range(series_count):
    series_name = input()
    series_price = float(input())

    if series_name == 'Thrones':
        final_price = series_price * 0.5
    elif series_name == 'Lucifer':
        final_price = series_price * 0.6
    elif series_name == 'Protector':
        final_price = series_price * 0.7
    elif series_name == 'TotalDrama':
        final_price = series_price * 0.8
    elif series_name == 'Area':
        final_price = series_price * 0.9
    else:
        final_price = series_price

    total_sum += final_price
    diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f'You bought all the series and left with {diff:.2f} lv.')
else:
    print(f'You need {diff:.2f} lv. more to buy the series!')