"""
С наближаването на световното първенство по снукър в театъра Крусибъл в Шефилд, Англия, феновете нямат търпение да
се сдобият с ценните билети. Заради големия наплив от хора, организаторите ви молят да напишете програма за
продаване на билети, като се има предвид следния ценоразпис:

	                Четвъртфинал	        Полуфинал	        Финал
Стандартен	    55.50 £/бр.	            75.88 £/бр.	        110.10 £/бр.
Премиум	        105.20 £/бр.	        125.22 £/бр.	    160.66 £/бр.
ВИП	            118.90 £/бр.	        300.40 £/бр.	    400 £/бр.

При закупуване на билет, зрителят може да избере опция, снимка с трофея, на цена 40 лири.
При достигане на определена сума има отстъпки:
•	Над 4000 лири има 25% отстъпка и безплатни снимки с трофея (ако  опцията за снимки е избрана,
таксата от 40 лири за билет не се включва)
•	Над 2500 лири има 10% отстъпка
При избрана опция за снимки с трофея, цената се начислява след изчисляването на отстъпките.
Вход
От конзолата се четат 3 реда:
1.	Етап на първенството – текст - “Quarter final ”, “Semi final” или “Final”
2.	Вид на билета – текст - “Standard”, “Premium” или “VIP”
3.	Брой билети – цяло число в интервала [1 … 30]
4.	Снимка с трофея – символ – 'Y' (да) или 'N' (не)
Изход
На конзолата се отпечатва 1 ред:
•	"Цената, която трябва да се заплати, форматирана до втората цифра след десетичния знак"
"""

competition_stage = input()
ticket_class = input()
tickets_count = int(input())
trophy_photo = input()

ticket_price = 0

if competition_stage == 'Quarter final':
    if ticket_class == 'Standard':
        ticket_price = 55.50
    elif ticket_class == 'Premium':
        ticket_price = 105.20
    elif ticket_class == 'VIP':
        ticket_price = 118.90
elif competition_stage == 'Semi final':
    if ticket_class == 'Standard':
        ticket_price = 75.88
    elif ticket_class == 'Premium':
        ticket_price = 125.22
    elif ticket_class == 'VIP':
        ticket_price = 300.40
elif competition_stage == 'Final':
    if ticket_class == 'Standard':
        ticket_price = 110.10
    elif ticket_class == 'Premium':
        ticket_price = 160.66
    elif ticket_class == 'VIP':
        ticket_price = 400

if trophy_photo == 'Y':
    ticket_price += 40
else:
    pass

total_income = tickets_count * ticket_price

if total_income > 4000:
    if trophy_photo == 'Y':
        ticket_price = ticket_price * 0.75
        print(f'{total_income:.2f}')

if 2000 < total_income <= 4000:
    ticket_price = 0.9
    if trophy_photo == 'Y':
        ticket_price += 40
        print(f'{total_income:.2f}')