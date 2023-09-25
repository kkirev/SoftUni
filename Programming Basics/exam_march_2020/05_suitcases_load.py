"""
https://judge.softuni.org/Contests/Practice/Index/2275#9

Напишете програма, която ви помага при товаренето на куфари в багажника на самолет. Всеки самолет има определен
капацитет на багажника. До получаване на команда "End" ще получавате обем на куфар. Обемът на всеки трети куфар
трябва да се увеличава с 10%, поради загубата на пространство при начина на подреждане. Ако свободното пространството

в даден момент е по-малко от обема на куфар товаренето трябва да прекъсне.
Вход
Първоначално се чете един ред:
•	Капацитетът на багажника – реално число в диапазона [100.0…6000.0]
След това до получаване на команда "End" или до запълване на багажника, се чете по един ред:

o	Обем на куфар – реално число в диапазона [100.0…6000.0]
Изход
На конзолата да се отпечатат следните редове според случая:
•	При получаване на командата "End" се печата:
"Congratulations! All suitcases are loaded!"
•	Ако обемът на куфара е по-голям от оставащото пространство в багажника:
"No more space!"
•	Накрая винаги се отпечатва статистика – колко багажа са натоварени:
"Statistic: {брой натоварени багажи} suitcases loaded."
"""

trunk_capacity = float(input())
command = input()

suitcases_count = 0
used_space = 0
full_trunk = False

while command != "End":
    suitcase_volume = float(command)
    suitcases_count += 1

    if suitcases_count % 3 == 0:
        suitcase_volume *= 1.1

    used_space += suitcase_volume

    if used_space > trunk_capacity:
        suitcases_count -= 1
        full_trunk = True
        break

    command = input()

if full_trunk:
    print(f'No more space!')
else:
    print(f'Congratulations! All suitcases are loaded!')

print(f'Statistic: {suitcases_count} suitcases loaded.')