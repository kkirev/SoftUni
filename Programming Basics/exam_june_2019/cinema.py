"""
https://judge.softuni.org/Contests/Practice/Index/1699#5

От кино ви наемат да напишете програма, чрез която да разберете дали на една прожекцията ще се запълни залата и колко
пари ще се изкарат от нея. Получавате места в залата и на всеки следващ ред до команда "Movie time!", колко хора влизат
в залата. Цената на един билет е 5 лв. Ако текущия брой хора влезли в залата се дели на 3 без остатък,
се прави отстъпка 5лв от общата им сметка.
Ако в залата се опитат да влязат повече хора от колкото места са останали, то се счита че местата са изчерпани и
програмата трябва да приключи четенето на вход.

Вход
От конзолата се четат:
•	На първия ред - капацитет на залата - цяло число в интервала [50... 150]
На всеки следващ ред до команда "Movie time!":
    o	Брой хора влизащи в киното - цяло число в интервала [1… 15]

Изход
На конзолата първо да се отпечата един ред:
•	При получена команда "Movie time!":
 "There are {останали места} seats left in the cinema."
•	При изчерпване на местата в залата:
	"The cinema is full."
След това да се отпечата:
	"Cinema income - {приходи от залата} lv."
"""

hall_capacity = int(input())
command = input()
cinema_income = 0
full_hall = False

while command != 'Movie time!':
    visitors_count = int(command)

    if visitors_count > hall_capacity:
        full_hall = True
        break

    hall_capacity -= visitors_count

    if visitors_count % 3 == 0:
        cinema_income += (visitors_count * 5) - 5
    else:
        cinema_income += visitors_count * 5

    command = input()

if command == 'Movie time!':
    print(f'There are {hall_capacity} seats left in the cinema.')

if full_hall:
    print(f'The cinema is full.')

print(f'Cinema income - {cinema_income} lv.')