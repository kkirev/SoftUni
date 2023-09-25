"""
Иван е измислил нова игра в която да се състезава със своите приятели. Вашата задача е да напишете програма за играта.
Всеки играч написва името си, след това за всяка една буква от името си написва по едно цяло число,
ако числото съвпада с ASCII стойността на съответната буква, играчът получава 10 точки, в противен случай,
получава само 2 точки. Победител е играчът с най-много точки в края на играта. В случай,
че двама играчи имат равен брой точки, печели този, който втори е достигнал резултата.

Вход
До получаване на командата "Stop" се чете по един ред:
•	Име на играча с дължина n - текст
За всеки играч се четат n на брой реда:
•	число – цяло число в интервала[0…127]

Изход
Да се отпечата един ред в следния формат:
•	"The winner is {името на победителя} with {точките на победителя} points!"
"""


current_points = 0
winner_points = 0
winner_name = ''

command = input()
while command != 'Stop':
    name = str(command)
    for letter in range(len(name)):
        letter_num = int(input())

        if letter_num == ord(name[letter]):
            current_points += 10
        else:
            current_points += 2

        if current_points >= winner_points:
            winner_points = current_points
            winner_name = name

    current_points = 0
    command = input()

print(f'The winner is {winner_name} with {winner_points} points!')