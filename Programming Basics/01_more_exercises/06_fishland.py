"""
https://judge.softuni.org/Contests/Practice/Index/1642#5

Георги ще има гости вечерта и решава да ги нагости с паламуд, сафрид и миди. Затова отива на рибната борса, за да си
купи по няколко килограма. Oт конзолата се въвеждат цените в лева на скумрията и цацата. Също количеството на паламуд,
сафрид и миди в килограми. Колко пари ще са му необходими, за да плати сметката си, ако цените на борсата са:
•	Паламуд – 60% по-скъп от скумрията
•	Сафрид – 80% по-скъп от цацата
•	Миди – 7.50 лв. за килограм

Вход
От конзолата се четат 5 числа:
•	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
•	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
•	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
•	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
•	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]

Изход
Да се отпечата на конзолата едно число с плаваща запетая: колко пари ще са нужни на Георги, за да си плати сметката.
Числото трябва да е форматирано до вторият знак след десетичната запетая (1.2457 -> 1.25).
"""
# паламуд = bonito
# скумрия = mackerel
# цаца = sprat

mackerel_price = float(input())
sprat_price = float(input())
bonito_kilos = float(input())
safrid_kilos = float(input())
mussels_kilos = int(input())

bonito_price = mackerel_price + mackerel_price * 0.6
safrid_price = sprat_price + sprat_price * 0.8
mussels_price = 7.5

bill = bonito_price * bonito_kilos + safrid_price * safrid_kilos + mussels_price * mussels_kilos
print("%.2f" % bill)