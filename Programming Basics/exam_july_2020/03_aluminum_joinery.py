# Фирма-производител на алуминиева дограма приема поръчки за изработката и монтаж със следния ценоразпис за един брой.
# Фирмата приема само поръчки на едро (над 10 бр.). В зависимост от поръчания брой дограми, фирмата прави различна
# отстъпка на своите клиенти.
# Фирмата предлага също и доставка на поръчките си срещу 60 лв.

# Размер	    Единична цена	    Отстъпка от цената
# 90X130	        110 лв.	        Над 30 броя – 5%
#                                   Над 60 броя – 8%

# 100X150	        140 лв.	        Над 40 броя – 6%
#                                   Над 80 броя – 10%

# 130X180	        190 лв.	        Над 20 броя – 7%
#                                   Над 50 броя – 12%

# 200X300	        250 лв.	        Над 25 броя – 9%
#                                   Над 50 броя – 14%
#
# Ако поръчката надвишава 99 броя  – върху крайната цена се начисляват допълнителни 4% отстъпка
# (след като се начисли цената за доставка, ако има такава).
# При поръчка под 10 бр. на конзолата да бъде изписано "Invalid order"

# Вход:
# Потребителят въвежда 3 реда:
# 1.	Брой дограми – цяло число в интервала [0..1000];
# 2.	Вид на дограмите – текст "90X130" или "100X150" или "130X180" или "200X300";
# 3.	Начин на получаване – текст
# •	С доставка - "With delivery"
# •	Без доставка - "Without delivery"

# Изход:
# Извежда се едно число – стойността на поръчката, в следния формат:
# o	"{Обща стойност на поръчката} BGN"
# Резултатът да се форматира до втори знак след десетичната запетая.

joinery_count = int(input())
joinery_size = input()
delivery = input()

joinery_price = 0
delivery_price = 0

if joinery_size == '90X130':
    joinery_price = 110
    if 30 < joinery_count <= 60:
        joinery_price *= 0.95
    elif joinery_count > 60:
        joinery_price *= 0.92

elif joinery_size == '100X150':
    joinery_price = 140
    if 40 < joinery_count <= 40:
        joinery_price *= 0.94
    if joinery_count > 80:
        joinery_price *= 0.90

elif joinery_size == '130X180':
    joinery_price = 190
    if 20 < joinery_count <= 50:
        joinery_price *= 0.93
    elif joinery_count > 50:
        joinery_price *= 0.88

elif joinery_size == '200X300':
    joinery_price = 250
    if 25 < joinery_count <= 50:
        joinery_price *= 0.91
    elif joinery_count > 50:
        joinery_price *= 0.86

if delivery == 'With delivery':
    delivery_price = 60
elif delivery == 'Without delivery':
    delivery_price = 0

total_sum = joinery_price * joinery_count + delivery_price

if joinery_count > 99:
    total_sum *= 0.96

if joinery_count < 10:
    print('Invalid order')
else:
    print(f'{total_sum:.2f} BGN')
