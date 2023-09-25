"""
https://judge.softuni.org/Contests/2418

Дадени са n цели числа в интервала [1…1000]. От тях някакъв процент p1 са под 200, друг процент p2 са от 200 до 399,
друг процент p3 са от 400 до 599, друг процент p4 са от 600 до 799 и останалите p5 процента са от 800 нагоре.
Да се напише програма, която изчислява и отпечатва процентите p1, p2, p3, p4 и p5.
Пример: имаме n = 20 числа: 53, 7, 56, 180, 450, 920, 12, 7, 150, 250, 680, 2, 600, 200, 800, 799, 199, 46, 128, 65.
"""

numbers_count = int(input())

numbers_sum = 0
p1_percents = 0
p2_percents = 0
p3_percents = 0
p4_percents = 0
p5_percents = 0

for numbers in range(numbers_count):
    current_number = int(input())
    numbers_sum += current_number
    if current_number < 200:
        p1_percents += 1
    elif current_number < 400:
        p2_percents += 1
    elif current_number < 600:
        p3_percents += 1
    elif current_number < 800:
        p4_percents += 1
    else:
        p5_percents += 1

print(f'{p1_percents / numbers_count * 100:.2f}%')
print(f'{p2_percents / numbers_count * 100:.2f}%')
print(f'{p3_percents / numbers_count * 100:.2f}%')
print(f'{p4_percents / numbers_count * 100:.2f}%')
print(f'{p5_percents / numbers_count * 100:.2f}%')