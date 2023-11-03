"""
https://judge.softuni.org/Contests/Practice/Index/1680#0

Екипът на СофтУни си организира футболен турнир. Първоначално прочитаме от конзолата капацитета на стадиона и броят
на всички фенове. След това за всеки фен се чете секторът, в който се намира. Феновете на първия отбор са в
сектор А и Б, а на втория – В и Г. Да се напише програма, която изчислява процентите на феновете във всеки сектор,
спрямо общия брой фенове на стадиона, както и общият процент на феновете за двата отбора,
спрямо капацитета на стадиона.
Общият брой на феновете НЕ надвишава капацитета на стадиона.
Вход
От конзолата се четат поредица от числа, всяко на отделен ред:
1.	Капацитетът на стадиона – цяло число в интервала [1 … 10000];
2.	Броят на всички фенове – цяло число в интервала [1 … 10000].
За всеки един фен, на отделен ред се прочита:
1.	Секторът, на който се намира – текст – "A", "B", "V" и "G".
Изход
Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00%,
форматирани до втората цифра след десетичната запетая:
1.	Процентът на феновете в сектор А
2.	Процентът на феновете в сектор Б
3.	Процентът на феновете в сектор В
4.	Процентът на феновете в сектор Г
5.	Процентът на всички фенове, спрямо капацитета на стадиона.
"""

# User input
stadium_capacity = int(input())
viewers_count = int(input())

team_1_viewers = 0
team_2_viewers = 0
viewers_a = 0
viewers_b = 0
viewers_v = 0
viewers_g = 0
total_viewers = 0

# Logic
for viewer in range(viewers_count):
    sector = input()

    if sector == 'A':
        team_1_viewers += 1
        viewers_a += 1
        total_viewers += 1
    elif sector == 'B':
        team_1_viewers += 1
        viewers_b += 1
        total_viewers += 1
    elif sector == 'V':
        team_2_viewers += 1
        viewers_v += 1
        total_viewers += 1
    elif sector == 'G':
        team_2_viewers += 1
        viewers_g += 1
        total_viewers += 1

percents_viewers_a = viewers_a / total_viewers * 100
percents_viewers_b = viewers_b / total_viewers * 100
percents_viewers_v = viewers_v / total_viewers * 100
percents_viewers_g = viewers_g / total_viewers * 100

viewers_per_capacity = total_viewers / stadium_capacity * 100

# Output
print(f'{percents_viewers_a:.2f}%')
print(f'{percents_viewers_b:.2f}%')
print(f'{percents_viewers_v:.2f}%')
print(f'{percents_viewers_g:.2f}%')
print(f'{viewers_per_capacity:.2f}%')