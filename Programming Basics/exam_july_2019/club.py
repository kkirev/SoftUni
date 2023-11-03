# Времето се затопля и клубовете пускат обещаващи промоции. Напише програма, която да изчислява приходите на един клуб
# за вечерта и дали е достигната желаната печалба, като знаете следните условия: цената на един коктейл е дължината
# неговото име. Ако цената на една поръчка е нечетно число, има 25% отстъпка от цената на поръчката.

# Вход
# От конзолата се четат:
# •	На първия ред – желаната печалба на клуба - реално число в интервала [1.00... 15000.00]
# Поредица от два реда до получаване на командата "Party!" или до достигане на желаната печалба:
# o	Име на коктейла – текст
# o	Брой на коктейлите за поръчката – цяло число в интервала [1… 50]

# Изход
# На конзолата първо да се отпечата един ред:
# •	При получена команда "Party!":
#  "We need {недостигаща сума} leva more."
# •	При достигане на желаната печалба:
# 	"Target acquired."
# След това да се отпечата:
# 	"Club income - {приходи от клуба} leva."
# Парите да бъдат форматирани до втората цифра след десетичния знак.

profit_target = float(input())
current_profit = 0
cocktail_price = 0
order_price = 0
profit_achieved = False

command = input()
while command != 'Party!':
    cocktail_name = command
    cocktails_count = int(input())
    cocktail_price = len(command)
    order_price = cocktails_count * cocktail_price

    if order_price % 2 != 0:
        order_price *= 0.75

    current_profit += order_price

    if current_profit >= profit_target:
        profit_achieved = True
        break
    command = input()

diff = profit_target - current_profit

if profit_achieved:
    print('Target acquired.')
    print(f'Club income - {current_profit:.2f} leva.')
else:
    print(f'We need {diff:.2f} leva more.')
    print(f'Club income - {current_profit:.2f} leva.')