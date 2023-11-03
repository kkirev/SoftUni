"""
https://judge.softuni.org/Contests/Compete/Index/2420#4

Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява
с колко най-малко монети може да стане това.
"""

change = float(input())
change = int(change * 100)
coins = 0

while change > 0.00:
    if change >= 200:
        change -= 200
    elif change >= 100:
        change -= 100
    elif change >= 50:
        change -= 50
    elif change >= 20:
        change -= 20
    elif change >= 10:
        change -= 10
    elif change >= 5:
        change -= 5
    elif change >= 2:
        change -= 2
    elif change >= 1:
        change -= 1

    coins += 1

print(coins)

# ----------------------------------
#
# change = float(input())
# coins = 0
#
# while change > 0.00:
#     if change >= 2.00:
#         change -= 2.00
#     elif change >= 1.00:
#         change -= 1.00
#     elif change >= 0.50:
#         change -= 0.50
#     elif change >= 0.20:
#         change -= 0.20
#     elif change >= 0.10:
#         change -= 0.10
#     elif change >= 0.05:
#         change -= 0.05
#     elif change >= 0.02:
#         change -= 0.02
#     elif change >= 0.01:
#         change -= 0.01
#
#     coins += 1
#
#     change = round(change, 2)
#
# print(coins)


