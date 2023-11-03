# Туристическа агенция има нужда от система за изчисляване на дължимата сума при резервация.
# В зависимост от различните дестинации и различните пакети, цената е различна.
# Цените за ден са следните:

# 	                    Банско/Боровец	                             Варна/Бургас
# 	              с екипировка	    без екипировка	        със закуска	    без закуска
# Цена за ден       100лв.	            80лв	                130лв.	        100лв.
# VIP отстъпка	    10%	                5%	                    12%	            7%

# Ако клиентът е заявил престой повече от 7 дни, получава единия ден безплатно.

# Вход
# От конзолата се четат 4 реда:
# 1.	Име на града - текст с възможности ("Bansko",  "Borovets", "Varna" или "Burgas")
# 2.	Вид на пакета - текст с възможности ("noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
# 3.	Притежание на VIP отстъпка - текст с възможности  "yes" или "no"
# 4.	Дни за престой - цяло число в интервала [1 … 10000]

# Изход
# На конзолата се отпечатва 1 ред:
# •	Когато потребителят е въвел всички данни правилно, отпечатваме:
# "The price is {цената, форматирана до втория знак}lv! Have a nice time!"
# •	Ако потребителят е въвел по-малко от 1 ден за престой, отпечатваме:
# "Days must be positive number!"
# •	Когато при въвеждането на града или вида на пакета се въведат невалидни данни, отпечатваме: "Invalid input!"

destination = input()
extras = input()
vip_card = input()
days_count = int(input())

price_per_day = 0
vip_discount = 0
FALSE_DATA = False

if days_count > 7:
    days_count -= 1

if destination == 'Bansko' or destination == 'Borovets':
    if extras == 'withEquipment':
        price_per_day = 100
        if vip_card == 'yes':
            vip_discount = 0.1
    elif extras == 'noEquipment':
        price_per_day = 80
        if vip_card == 'yes':
            vip_discount = 0.05
    else:
        FALSE_DATA = True
elif destination == 'Varna' or destination == 'Burgas':
    if extras == 'withBreakfast':
        price_per_day = 130
        if vip_card == 'yes':
            vip_discount = 0.12
    elif extras == 'noBreakfast':
        price_per_day = 100
        if vip_card == 'yes':
            vip_discount = 0.07
    else:
        FALSE_DATA = True
else:
    FALSE_DATA = True

final_price = days_count * price_per_day * (1 - vip_discount)

if days_count < 1:
    print(f'Days must be positive number!')
elif FALSE_DATA:
    print(f'Invalid input!')
else:
    print(f'The price is {final_price:.2f}lv! Have a nice time!')