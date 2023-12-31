"""
https://judge.softuni.org/Contests/Practice/Index/1654#4

Дадени са n цели числа в интервала [1…1000]. От тях някакъв процент p1 се делят без остатък на 2,
друг процент p2 се делят без остатък на 3, друг процент p3 се делят без остатък на 4. Да се напише програма,
която изчислява и отпечатва процентите p1, p2 и p3.
Пример: имаме n = 10 числа: 680, 2, 600, 200, 800, 799, 199, 46, 128, 65.
Получаваме следното разпределение и визуализация:

Деление без             Числа в диапазона	                    Брой числа	                Процент
остатък на:
    2	            680, 2, 600, 200, 800, 46, 128	                7	            p1 = 7.0 / 10 * 100 = 70.00%
    3	            600	                                            1	            p2 = 1 / 10 * 100 = 10.00%
    4	            680, 600, 200, 800, 128	                        5	            p3 = 5 / 10 * 100 = 50.00%

Вход
На първия ред от входа стои цялото число n (1 ≤ n ≤ 1000) – брой числа.
На следващите n-на брой реда стои по едно цяло число в интервала [1…1000] – числата,
 които да бъдат проверени на колко се делят.

Изход
Да се отпечатат на конзолата 3 реда, всеки от които съдържа процент между 0% и 100%,
с точност две цифри след десетичната точка, например 25.00%, 66.67%, 57.14%.
•	На първият ред – процентът на числата които се делят на 2
•	На вторият ред – процентът на числата които се делят на 3
•	На третият ред – процентът на числата които се делят на 4
"""

numbers_count = int(input())
div_by_2 = 0
div_by_3 = 0
div_by_4 = 0

for num in range(numbers_count):
    num = int(input())
    if num % 2 == 0:
        div_by_2 += 1
    if num % 3 == 0:
        div_by_3 += 1
    if num % 4 == 0:
        div_by_4 += 1

percent_div_by_2 = div_by_2 / numbers_count * 100
percent_div_by_3 = div_by_3 / numbers_count * 100
percent_div_by_4 = div_by_4 / numbers_count * 100

print(f'{percent_div_by_2:.2f}%')
print(f'{percent_div_by_3:.2f}%')
print(f'{percent_div_by_4:.2f}%')