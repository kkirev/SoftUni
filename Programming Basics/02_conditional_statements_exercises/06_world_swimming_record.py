"""
https://judge.softuni.org/Contests/Compete/Index/2414#5

Иван решава да подобри Световния рекорд по плуване на дълги разстояния. На конзолата се въвежда рекордът в секунди,
който Иван трябва да подобри,  разстоянието в метри, което трябва да преплува и времето в секунди, за което плува
разстояние от 1 м. Да се напише програма, която изчислява дали се е справил със задачата,като се има предвид, че:
съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди. Когато се изчислява колко пъти Иван ще се забави,
в резултат на съпротивлението на водата, резултатът трябва да се закръгли надолу до най-близкото цяло число.
Да се изчисли времето в секунди, за което Иван ще преплува разстоянието и разликата спрямо Световния рекорд.

Вход
От конзолата се четат 3 реда:
1.	Рекордът в секунди – реално число;
2.	Разстоянието в метри – реално число;
3.	Времето в секунди, за което плува разстояние от 1 м. - реално число.

Изход
Отпечатването на конзолата зависи от резултата:
•	Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
    o	" Yes, he succeeded! The new world record is {времето на Иван} seconds."
•	Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:
    o	"No, he failed! He was {недостигащите секунди} seconds slower."
Резултатът трябва да се форматира до втория знак след десетичната запетая.
"""

record = float(input())                 # Current world record
distance_in_meters = float(input())     # Distance which must cross
time_per_meter_in_sec = float(input())  # Time in seconds to swim 1 meter

total_slowdown = (distance_in_meters // 15) * 12.5
total_swim_time = time_per_meter_in_sec * distance_in_meters + total_slowdown
difference = abs(record - total_swim_time)

if total_swim_time < record:
    print(f'Yes, he succeeded! The new world record is {total_swim_time:.2f} seconds.')
else:
    print(f' No, he failed! He was {difference:.2f} seconds slower.')