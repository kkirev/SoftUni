"""
https://judge.softuni.org/Contests/Practice/Index/1381#0

Напишете програма, която да принтира на конзолата всички комбинации от 3 букви в зададен интервал, като се пропускат
комбинациите съдържащи зададена от конзолата буква. Накрая трябва да се изпринтира броят на отпечатаните комбинации.

Вход
Входът се чете от конзолата и съдържа точно 3 реда:
Ред 1.	Малка буква от английската азбука за начало на интервала – от ‘a’ до ‚z’.
Ред 2.	Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
Ред 3.	Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.

Изход
Да се отпечатат на един ред всички комбинации отговарящи на условието плюс броят им разделени с интервал.
"""

# start_interval = input()
# end_interval = input()
# avoid_letter = input()
# combination_counter = 0
#
# for letter_one in range(ord(start_interval), ord(end_interval) + 1):
#     for letter_two in range(ord(start_interval), ord(end_interval) + 1):
#         for letter_three in range(ord(start_interval), ord(end_interval) + 1):
#             if letter_one != avoid_letter and letter_two != avoid_letter and letter_three != avoid_letter:
#                 combination_counter += 1

#                 print(chr(letter_one),chr(letter_two),chr(letter_three), sep='', end=' ',)
#
# НЕЗАВЪРШЕНА ЗАДАЧА, ЗАЦИКЛИХ И НЕ ЗНАМ КАК ДА ПРОДЪЛЖА

starting_letter = input()
ending_letter = input()
skip_letter = input()

counter = 0

for one in range(ord(starting_letter), ord(ending_letter) + 1):
    for two in range(ord(starting_letter), ord(ending_letter) + 1):
        for three in range(ord(starting_letter), ord(ending_letter) + 1):
            combination = chr(one) + chr(two) + chr(three)
            if skip_letter in str(combination):
                continue
            else:
                counter += 1

            print(combination, end=' ')
print(counter)