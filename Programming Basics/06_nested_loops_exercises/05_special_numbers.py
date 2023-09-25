# Да се напише програма, която чете едно цяло число N, въведено от потребителя, и генерира всички възможни "специални"
# числа от 1111 до 9999. За да бъде “специално” едно число, то трябва да отговаря на следното условие:
# •	N да се дели на всяка една от неговите цифри без остатък.
# Пример: при N = 16, 2418 е специално число:
# •	16 / 2 = 8 без остатък
# •	16 / 4 = 4 без остатък
# •	16 / 1 = 16 без остатък
# •	16 / 8 = 2 без остатък

# Вход
# Входът се чете от конзолата и се състои от едно цяло число в интервала [1…600000]

# Изход
# На конзолата трябва да се отпечатат всички “специални” числа, разделени с интервал

number = int(input())

for curr_num in range(1111, 9999 + 1):
    is_special = True
    num_to_str = str(curr_num)
    for index in range(len(num_to_str)):
        curr_index = int(num_to_str[index])
        if curr_index == 0 or number % curr_index != 0:
            is_special = False
            break

    if is_special:
        print(curr_num, end=' ')

# -----------------------------------------------------------------------------------------
#
# number = int(input())
#
# for digit_1 in range(1, 9):
#     if number % digit_1 == 0:
#
#         for digit_2 in range(1, 9):
#             if number % digit_2 == 0:
#
#                 for digit_3 in range(1, 9):
#                     if number % digit_3 == 0:
#
#                         for digit_4 in range(1, 9):
#                             if number % digit_4 == 0:
#
#                                 print(f"{digit_1}{digit_2}{digit_3}{digit_4}", end=" ")