"""
https://judge.softuni.org/Contests/Practice/Index/1637#6

На Великден семейството на Деси се събира и тя решава да организира "битка" между великденски яйца.
Правилата на "битката" са следните:
•	Участват двама играчи
•	Всеки от тях започва с определен брой яйца
•	При получаване на команда "one" -> първият играч печели => яйцата на втория намаляват с едно
•	При получаване на команда "two" -> вторият играч печели => яйцата на първия намаляват с едно
•	Играта приключва, ако някой от играчите остане без яйца или до получаване на команда "End"

Вход
Първоначално се четат два реда:
1.	Брой яйца, които има първият играч - цяло число в интервала [1 … 99]
2.	Брой яйца, които има вторият играч - цяло число в интервала [1 … 99]
След това до получаване на команда "End" се четe многократно един ред:
3.	Победител - текст - "one" или "two"

Изход
Ако първият играч остане без яйца:
•	"Player one is out of eggs. Player two has {брой останали яйца на втория играч} eggs left."
Ако вторият играч остане без яйца:
•	"Player two is out of eggs. Player one has {брой останали яйца на първия играч} eggs left."
При команда "End" да се отпечатат два реда:
•	"Player one has {брой останали яйца на първия играч} eggs left."
•	"Player two has {брой останали яйца на втория играч} eggs left."
"""

player_one_eggs = int(input())
player_two_eggs = int(input())
command = input()

player_one_wins = 0
player_two_wins = 0
player_one_loose = False
player_two_loose = False

while command != 'End':
    winner = command

    if winner == 'one':
        player_one_wins += 1
        player_two_eggs -= 1
    elif winner == 'two':
        player_two_wins += 1
        player_one_eggs -= 1

    if player_one_eggs == 0:
        player_one_loose = True
        break
    elif player_two_eggs == 0:
        player_two_loose = True
        break

    command = input()

if player_one_loose:
    print(f'Player one is out of eggs. Player two has {player_two_eggs} eggs left.')
elif player_two_loose:
    print(f'Player two is out of eggs. Player one has {player_one_eggs} eggs left.')
else:
    print(f'Player one has {player_one_eggs} eggs left.')
    print(f'Player two has {player_two_eggs} eggs left.')