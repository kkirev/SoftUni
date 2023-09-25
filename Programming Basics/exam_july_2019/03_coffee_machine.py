# Напишете софтуер, който да пресмята сметката на клиент, закупил определен брой от дадена напитка от кафемашина.

# 	            Без захар	    Нормално	    Допълнително захар
# Еспресо	    0.90 лв./бр.	1 лв. /бр.	    1.20 лв. /бр.
# Капучино	    1.00 лв. /бр.	1.20 лв. /бр.	1.60 лв. /бр.
# Чай	        0.50 лв. /бр.	0.60 лв. /бр.	0.70 лв. /бр.

# Трябва да имате предвид следните отстъпки:
# •	При избрана напитка без захар има 35% отстъпка.
# •	При избрана напитка "Espresso" и закупени поне 5 броя, има 25% отстъпка.
# •	При сума надвишава 15 лева, 20% отстъпка от крайната цена,
# Отстъпките се прилагат в реда на тяхното описване.

# Вход
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред - напитка - текст с възможности"Espresso", "Cappuccino" или "Tea"
# •	Втори ред - захар - текст  с възможности "Without", "Normal" или "Extra"
# •	Трети ред - брой напитки - цяло число в интервала [1… 50]

# Изход
# На конзолата трябва да се отпечата един ред:
# "You bought {брой напитки} cups of {напитка} for {крайна цена} lv."
# Цената да бъде форматирана до втората цифра след десетичния знак.

type_of_drink = input()
sugar_amount = input()
count_drinks = int(input())

price_drink = 0
if type_of_drink == "Espresso":
    if sugar_amount == "Without":
        price_drink = 0.9
    elif sugar_amount == "Normal":
        price_drink = 1
    elif sugar_amount == "Extra":
        price_drink = 1.2

if type_of_drink == "Cappuccino":
    if sugar_amount == "Without":
        price_drink = 1
    elif sugar_amount == "Normal":
        price_drink = 1.2
    elif sugar_amount == "Extra":
        price_drink = 1.6

if type_of_drink == "Tea":
    if sugar_amount == "Without":
        price_drink = 0.5
    elif sugar_amount == "Normal":
        price_drink = 0.6
    elif sugar_amount == "Extra":
        price_drink = 0.7

bill = count_drinks * price_drink

if sugar_amount == "Without":
    bill *= 0.65
if type_of_drink == "Espresso" and count_drinks >= 5:
    bill *= 0.75
if bill > 15:
    bill *= 0.8

print(f'You bought {count_drinks} cups of {type_of_drink} for {bill:.2f} lv.')