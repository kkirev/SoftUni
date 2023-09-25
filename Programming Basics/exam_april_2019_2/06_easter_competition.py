"""
https://judge.softuni.org/Contests/Practice/Index/1637#10

С наближаването на Великден, пекарна организира конкурс за направата на най-хубав козунак. Напишете програма, която да
намира сладкаря с най-висок резултат. В началото на конкурса се въвежда броя на козунаците, които ще бъдат дегустирани
от посетителите на пекарната, като за всеки козунак различен брой посетители, ще дадат оценка от 1 до 10.

Вход
Първоначално от конзолата се прочита броя на козунаците – цяло число в интервала [1… 100]
След това за всеки козунак се прочита:
•	Името на пекаря, който е направил козунака – текст
•	До получаване на командата "Stop" се прочита
    o	оценка за козунак от един човек  – цяло число в интервала [1... 10]

Изход
След получаване на командата "Stop" се печата един ред:
•	"{името на пекаря} has {общият брой получени точки} points."
Ако след командата "Stop", пекарят е с най-много точки до момента, да се отпечата допълнителен ред:
•	"{името на пекаря} is the new number 1!"
След дегустация на всички козунаци, да се отпечата един ред:
•	"{името на пекаря с най-много точки} won competition with {точките на пекаря} points!"
"""

easter_bread_count = int(input())
best_baker_score = 0
best_baker = ''

for bread in range(easter_bread_count):
    current_baker_score = 0
    baker_name = input()
    command = input()

    while command != 'Stop':
        bread_rate = int(command)
        current_baker_score += bread_rate
        command = input()

        if command == 'Stop':
            print(f'{baker_name} has {current_baker_score} points.')
            if current_baker_score > best_baker_score:
                best_baker_score = current_baker_score
                best_baker = baker_name
                print(f'{baker_name} is the new number 1!')

print(f'{best_baker} won competition with {best_baker_score} points!')

