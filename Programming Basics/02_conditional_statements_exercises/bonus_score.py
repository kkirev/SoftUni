"""
https://judge.softuni.org/Contests/Compete/Index/2414#1

Дадено е цяло число – начален брой точки. Върху него се начисляват бонус точки по правилата, описани по-долу.
Да се напише програма, която пресмята бонус точките, които получава числото и общия брой точки (числото + бонуса).
•	Ако числото е до 100 включително, бонус точките са 5;
•	Ако числото е по-голямо от 100, бонус точките са 20% от числото;
•	Ако числото е по-голямо от 1000, бонус точките са 10% от числото.
•	Допълнителни бонус точки (начисляват се отделно от предходните):
o	За четно число  + 1 т.
o	За число, което завършва на 5  + 2 т.

"""
points = int(input())
bonus = 0

# Тук проверяваме в кой диапазон е въведеното число
if points <= 100:
    bonus = 5
elif points > 1000:
    bonus = points * 0.1
else:
    bonus = points * 0.2

# Тук проверяваме дали въвденото число е четно и дали завършва на 5
if points % 2 == 0:
    bonus += 1
elif points % 10 == 5:
    bonus += 2

print(bonus)
print(points + bonus)