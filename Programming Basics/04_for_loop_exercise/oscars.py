"""
https://judge.softuni.org/Contests/2418

Поканени сте от академията да напишете софтуер, който да пресмята точките за актьор/актриса.
Академията ще ви даде първоначални точки за актьора. След това всеки оценяващ ще дава своята оценка.
Точките, които актьора получава се формират от: дължината на името на оценяващия умножено по точките,
които дава делено на две.
Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне и да се отпечата,
че дадения актьор е получил номинация.

Вход
•	Име на актьора - текст
•	Точки от академията - реално число в интервала [2.0... 450.5]
•	Брой оценяващи n - цяло число в интервала[1… 20]
На следващите n-на брой реда:
    o	Име на оценяващия - текст
    o	Точки от оценяващия - реално число в интервала [1.0... 50.0]

Изход
Да се отпечата на конзолата един ред:
•	Ако точките са над 1250.5:
"Congratulations, {име на актьора} got a nominee for leading role with {точки}!"
•	Ако точките не са достатъчни:
	"Sorry, {име на актьора} you need {нужни точки} more!"
Резултатът да се форматирана до първата цифра след десетичния знак!
"""

actor_name = input()
academy_points = float(input())
jury_count = int(input())

nomination_points = 1250.5

for jury in range(jury_count):
    jury_name = input()
    jury_points = float(input())
    academy_points += len(jury_name) * jury_points / 2

    if academy_points + jury_points > nomination_points:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
        break

if academy_points <= 1250.5:
    print(f'Sorry, {actor_name} you need {nomination_points - academy_points:.1f} more!')