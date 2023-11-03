"""
https://judge.softuni.org/Contests/2418

Напишете програма, която отпечатва числата в диапазона от 1 до 1000, които завършват на 7.
"""

# for number in range(1, 1000):
#     if number % 10 == 7:
#         print(number)

for number in range(7, 1000, 10):
    print(number)