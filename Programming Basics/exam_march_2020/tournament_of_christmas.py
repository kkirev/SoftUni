"""
https://judge.softuni.org/Contests/Practice/Index/2275#10

Напишете програма, която проследява представянето на вашия отбор на благотворителен коледен турнир.
Всеки ден получавате имена на игри до команда "Finish". Със спечелването на всяка една игра печелите по 20лв. за
благотворителност. Трябва да изчислите колко пари сте спечелили на края на деня. Ако имате повече спечелени игри,
отколкото загубени – вие сте победители този ден и увеличавате парите от него с 10%. При приключване на турнира
ако през повечето дни сте били победители печелите турнира и увеличавате всичките спечелени пари с 20%.
Никога няма да имате равен брой спечелени и загубени игри.

Вход:
Първоначално от конзолата се прочита броя дни на турнира – цяло число в интервала [1… 20]
До получаване на командата "Finish" се чете:
•	Спорт  – текст
За всеки спорт се прочита:
•	Резултат  – текст с възможности: "win" или "lose"

Изход:
Накрая се отпечатва един ред:
•	Ако сте спечелили турнира:
    "You won the tournament! Total raised money: {спечелените пари}"
•	Ако сте загубили на турнира:
    "You lost the tournament! Total raised money: {спечелените пари}"
Парите да бъдат форматирани до втората цифра след десетичния знак.
"""

tournament_days = int(input())

wins = 0
loses = 0
win_days = 0
lose_days = 0
daily_money_won = 0
total_money_won = 0

for day in range(1, tournament_days + 1):
    command = input()
    while command != 'Finish':
        sport = command
        result = input()

        if result == "win":
            daily_money_won += 20
            wins += 1
        elif result == "lose":
            loses += 1

        command = input()

    if wins > loses:
        win_days += 1
        daily_money_won *= 1.10
    else:
        lose_days += 1

    total_money_won += daily_money_won
    wins = 0
    loses = 0
    daily_money_won = 0

if win_days > lose_days:
    total_money_won *= 1.2
    print(f'You won the tournament! Total raised money: {total_money_won:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money_won:.2f}')