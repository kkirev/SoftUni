"""
https://judge.softuni.org/Contests/Practice/Index/1654#2

Мобилен оператор предлага договори с различна месечна такса в зависимост от срока - 1 или 2 години.
Да се напише програма, която изчислява дължимата сума, която трябва да се плати за определен брой месеци.

  срок / тип	      Small	         Middle	         Large	        ExtraLarge
1 година(one)	    9.98 лв.	    18.99 лв.	    25.98 лв.	    35.99 лв.
2 години(two)	    8.58 лв.	    17.09 лв.	    23.59 лв.	    31.79 лв.

Условия:
•	при добавен мобилен интернет, към таксата за един месец се добавя:
o	при такса по-малка или равна на 10.00 лв.  5.50 лв.
o	при такса по-малка или равна на 30.00 лв.  4.35 лв.
o	при такса по-голяма от 30.00 лв.  3.85 лв.
•	ако договорът e за две години, общата сума се намалява с 3.75%

Вход
От конзолата се четат 3 реда:
1.	Срок на договор – текст – "one", или "two"
2.	Тип на договор – текст – "Small",  "Middle", "Large"или "ExtraLarge"
3.	Добавен мобилен интернет – текст – "yes" или "no"
4.	Брой месеци за плащане - цяло число в интервала [1 … 24]

Изход
На конзолата се отпечатва 1 ред:
• Цената, която заплаща клиентът, форматирана до втория знак след десетичната запетая, в следния формат:  "{цената} lv."
"""

contract_duration = input()
contract_type = input()
internet_included = input()
months_to_pay = int(input())

monthly_fee = 0
internet_fee = 0

if contract_duration == 'one':
    if contract_type == 'Small':
        monthly_fee = 9.98
    elif contract_type == 'Middle':
        monthly_fee = 18.99
    elif contract_type == 'Large':
        monthly_fee = 25.98
    elif contract_type == 'ExtraLarge':
        monthly_fee = 35.99
elif contract_duration == 'two':
    if contract_type == 'Small':
        monthly_fee = 8.58
    elif contract_type == 'Middle':
        monthly_fee = 17.09
    elif contract_type == 'Large':
        monthly_fee = 23.59
    elif contract_type == 'ExtraLarge':
        monthly_fee = 31.79

if internet_included == 'yes':
    if monthly_fee <= 10:
        internet_fee = 5.5
    elif 10 < monthly_fee <= 30:
        internet_fee = 4.35
    else:
        internet_fee = 3.85
elif internet_included == 'no':
    internet_fee = 0

sum_to_pay = months_to_pay * (monthly_fee + internet_fee)

if contract_duration == 'two':
    sum_to_pay *= 0.9625

print(f'{sum_to_pay:.2f} lv.')