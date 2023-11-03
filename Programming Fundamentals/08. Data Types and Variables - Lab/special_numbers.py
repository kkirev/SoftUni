"""
Write a program that reads an integer n. Then, for all numbers in the range [1, n], prints the number and if it is
special or not (True / False). A number is special when the sum of its digits is 5, 7, or 11.

Examples:
    Input   Output
        1   1 -> False
            2 -> False
            3 -> False
            4 -> False
            5 -> True
            6 -> False
            7 -> True
            8 -> False
            9 -> False
            10 -> False
            11 -> False
            12 -> False
            13 -> False
            14 -> True
            15 -> False

    Input   Output
        6
            1 -> False
            2 -> False
            3 -> False
            4 -> False
            5 -> True
            6 -> False
"""

number = int(input())
for current_number in range(1, number + 1):
    current_number_as_string = str(current_number)
    digits_sum = 0

    for digit in current_number_as_string:
        digits_sum += int(digit)
    is_special = False

    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        is_special = True

    print(f"{current_number} -> {is_special}")