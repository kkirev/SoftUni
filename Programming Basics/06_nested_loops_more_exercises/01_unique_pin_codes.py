# https://judge.softuni.org/Contests/Practice/Index/1381#0

# 1. Уникални PIN кодове
# Да се напише програма, която генерира трицифрени PIN кодове, като цифрите на всеки PIN код са в определен интервал.
# За да бъде валиден един PIN код той трябва да отговаря на следните условия:
# •	Първата и третата цифра трябва да бъдат четни.
# •	Втората цифра трябва да бъде просто число в диапазона [2...7].

# Вход
# От конзолата се четат 3 реда:
# •	Горната граница на първото число - цяло число в диапазона [1...9]
# •	Горната граница на второто число - цяло число в диапазона [1...9]
# •	Горната граница на третото число - цяло число в диапазона [1...9]

# Изход
# Да се отпечатат на конзолата всички валидни трицифрени PIN кодове, чиито цифри отговарят на съответните интервали.

upper_limit_1 = int(input())
upper_limit_2 = int(input())
upper_limit_3 = int(input())

for digit_1 in range(2, upper_limit_1+1, 2):
    for digit_2 in range(2, upper_limit_2 + 1):
        if digit_2 == 2 or digit_2 == 3 or digit_2 == 5 or digit_2 == 7:
            for digit_3 in range(2, upper_limit_3 + 1, 2):
                print(f"{digit_1} {digit_2} {digit_3}")

# pin_one = int(input())
# pin_two = int(input())
# pin_three = int(input())
#
# for num_one in range(1, pin_one + 1):
#     for num_two in range(1, pin_two + 1):
#         for num_three in range(1, pin_three + 1):
#             if num_one % 2 == 0 and num_three % 2 == 0 and str(num_two) in "2357":
#                 print(f"{num_one} {num_two} {num_three}")
