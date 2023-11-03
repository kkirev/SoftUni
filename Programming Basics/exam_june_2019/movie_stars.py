"""
https://judge.softuni.org/Contests/Practice/Index/1699#6

Счетоводителят на киноцентър "Тинтява 15" ви наема да напишете програма, която пресмята хонорарите за актьорите.
Всяка продукция има бюджет за актьори. До команда "ACTION" ще получавате име на актьор и възнаграждението му.
Ако името на актьора е по-дълго от 15 символа възнаграждението му ще е 20 % от останалия бюджет до момента.
Ако бюджета в даден момент свърши, програмата трябва да прекъсне.

Вход
От конзолата първо се чете един ред:
•	Бюджет за актьори - реално число в интервала [1000.0... 2 100 000.0]
След това се четат многократно по един или два реда до команда "ACTION" или до изчерпване на бюджета:
•	Име на актьор - текст
Ако името на актьора съдържа по-малко или равно на 15 брой символи:
    o	Възнаграждение - реално число в интервала [250.0… 1 000 000.0]

Изход
На конзолата да се отпечата един ред:
•	Ако бюджета е достатъчен :
             "We are left with {останал бюджет} leva."
•	Ако бюджета не е достатъчен:
	"We need {необходим бюджет} leva for our actors."
Резултата да се форматира до втората цифра след десетичния знак!
"""

actors_budget = float(input())
no_more_money = False

command = input()
while command != 'ACTION':
    actor_name = command

    if len(actor_name) <= 15:
        actor_payment = float(input())
        if actor_payment >= actors_budget:
            no_more_money = True
            diff = abs(actor_payment - actors_budget)
            break
    else:
        actor_payment = 0.2 * actors_budget
        if actor_payment >= actors_budget:
            no_more_money = True
            break

    actors_budget -= actor_payment
    command = input()

if no_more_money:
    print(f'We need {diff:.2f} leva for our actors.')
else:
    print(f'We are left with {actors_budget:.2f} leva.')

# --------------------------------------------------------------------------------
# actors_budget = float(input())
# command = input()
#
# while command != 'ACTION':
#     actor_name = command
#
#     if len(actor_name) > 15:
#         actor_payment = 0.2 * actors_budget
#     else:
#         actor_payment = float(input())
#
#     if actors_budget < actor_payment:
#         diff = abs(actors_budget - actor_payment)
#         print(f'We need {diff:.2f} leva for our actors.')
#         break
#
#     actors_budget -= actor_payment
#     command = input()
#
# if command == 'ACTION' and actors_budget > 0:
#     print(f'We are left with {actors_budget:.2f} leva.')