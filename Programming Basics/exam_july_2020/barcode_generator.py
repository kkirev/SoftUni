"""
Техниката в магазин за коледни украси се разваля. Артикулите, които съдържат четни числа в своя баркод не могат да
бъдат маркирани от касиерите. Вашата задача е, да напишете програма, която генерира всички баркодове,
които НЕ съдържат четни цифри в себе си.

Вход:
•	Две четирицифрени числа, които показват обхвата на баркодовете, които трябва да промените.
•	Първи ред – четирицифрено число – началото на обхвата. Цяло число в интервала [1000…9999]
•	Втори ред – четирицифрено число – края на обхвата. Цяло число в интервала [1000…9999]

Изход:
На конзолата трябва да се отпечатат всички "баркодове", които НЕ съдържат четна цифра в себе си, разделени с интервал.
"""

start_interval = int(input())
end_interval = int(input())

for digit_1 in range(int(str(start_interval)[0]), int(str(end_interval)[0]) + 1):
    for digit_2 in range(int(str(start_interval)[1]), int(str(end_interval)[1]) + 1):
        for digit_3 in range(int(str(start_interval)[2]), int(str(end_interval)[2]) + 1):
            for digit_4 in range(int(str(start_interval)[3]), int(str(end_interval)[3]) + 1):
                if digit_1 % 2 != 0 and digit_2 % 2 != 0 and digit_3 % 2 != 0 and digit_4 % 2 != 0:

                    print(f'{digit_1}{digit_2}{digit_3}{digit_4}', end=' ')

#-------------------------------------------------------------------------------------------------------------
# start_interval = int(input())
# end_interval = int(input())
#
# for digit_1 in range(start_interval // 1000, end_interval // 1000 + 1):

#     for digit_2 in range(start_interval % 1000 // 100, end_interval % 1000 // 100 + 1):

#         for digit_3 in range(start_interval % 100 // 10, end_interval % 100 // 10 + 1):

#             for digit_4 in range(start_interval % 10, end_interval % 10 + 1):

#                 if digit_1 % 2 != 0 and digit_2 % 2 != 0 and digit_3 % 2 != 0 and digit_4 % 2 != 0:

#                     print(f"{digit_1}{digit_2}{digit_3}{digit_4}", end=" ")

#-------------------------------------------------------------------------------------------------------------

# first_number = input()
# second_number = input()
#
# for l in range(int(first_number[0]), int(second_number[0]) + 1):
#     if l % 2 == 0:
#         continue
#
#     for k in range(int(first_number[1]), int(second_number[1]) + 1):
#         if k % 2 == 0:
#             continue
#
#         for j in range(int(first_number[2]), int(second_number[2]) + 1):
#             if j % 2 == 0:
#                 continue
#
#             for s in range(int(first_number[3]), int(second_number[3]) + 1):
#                 if s % 2 != 0:
#                     print(f'{l}{k}{j}{s}', end=' ')