"""
https://judge.softuni.org/Contests/Practice/Index/1684#0

На благотворително събитие плащанията за закупените продукти винаги се редуват: плащане в брой и плащане с карта.
Установени са следните правила за заплащане:
•	Ако продуктът надвишава 100лв., за него не може да се плати в брой
•	Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
Програмата приключва или след като получим команда "End" или след като средствата бъдат събрани.
Вход
От конзолата се четат:
•	Сумата, която се очаква да бъде събрана от продажбите - цяло число в интервала [1 ... 10000]
На всеки следващ ред, до получаване на командата "End" или докато не се съберат нужните средства:
цените на предметите, които ще бъдат закупени - цяло число в интервала [1 ... 500]
Изход
На конзолата да се отпечата:
•	При успешна транзакция: "Product sold!"
•	При неуспешна транзакция: "Error in transaction!"
•	Ако сумата на всички закупени продукти надвиши или достигне очакваната сума, програмата трябва да приключи
и на конзолата да се изпишат два реда:
o	"Average CS: {средно плащане в кеш на човек}"
o	"Average CC: {средно плащане с карта на човек}"
              Плащанията трябва да бъдат форматирани до втората цифра след десетичния знак.
•	При получаване на команда "End", да се изпише един ред:
o	"Failed to collect required money for charity."
"""

goal_sum = int(input())
command = input()

payment_type = 0 # 1 е плащане с кеш, 2 е плащане с карта
cash_payment = 0
card_payment = 0
cash_count = 0
card_count = 0

while command != "End":
    payment_type += 1
    product_price = int(command)
# логика за неуспешни плащания
    if product_price > 100 and payment_type == 1:
        print("Error in transaction!")
    elif product_price <= 10 and payment_type == 2:
        print("Error in transaction!")
# логика за успешни плащания
    if product_price <= 100 and payment_type == 1:
        cash_payment += product_price
        cash_count += 1
        print("Product sold!")
    elif product_price > 10 and payment_type == 2:
        card_payment += product_price
        card_count += 1
        print("Product sold!")
# логика ако плащанията са достатъчни
    total_payment = card_payment + cash_payment
    if total_payment >= goal_sum:
        print(f"Average CS: {cash_payment/cash_count:.2f}")
        print(f"Average CC: {card_payment / card_count:.2f}")
        break
# ресетване метода на плащане
    if payment_type == 2:
        payment_type = 0

    command = input()

else:
    print("Failed to collect required money for charity.")