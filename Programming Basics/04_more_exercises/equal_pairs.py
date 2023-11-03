"""
https://judge.softuni.org/Contests/Practice/Index/1680#0

Дадени са 2*n-на брой числа. Първото и второто формират двойка, третото и четвъртото също и т.н.
Всяка двойка има стойност – сумата от съставящите я числа. Напишете програма, която проверява дали всички
двойки имат еднаква стойност или печата максималната разлика между две последователни двойки.
Ако всички двойки имат еднаква стойност, отпечатайте "Yes, value={Value}" + стойността.
В противен случай отпечатайте "No, maxdiff={Difference}" + максималната разлика.
"""

pairs_count = int(input())
previous_sum = int(input()) + int(input())
max_diff = 0

for _ in range(pairs_count - 1): # -1 защото първата двойка вече е вписана като previous_sum, още в началния input
    current_sum = int(input()) + int(input())
    sum_diff = abs(previous_sum - current_sum)
    if sum_diff > max_diff:
        max_diff = sum_diff

    previous_sum = current_sum #в тялото на цикъла презаписваме променливата previous_sum

if max_diff == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_diff}")

# -----------------------------------------------------

# pairs_count = int(input())
#
# curr_pair_sum = 0
# previous_sum = 0
# max_diff = 0
#
# for i in range(2 * pairs_count):
#     curr = int(input())
#     curr_pair_sum += curr
#
#     if i % 2 != 0 and i >= 3:
#         pairs = abs(curr_pair_sum - previous_sum)
#         if max_diff < pairs:
#             max_diff = pairs
#         previous_sum = curr_pair_sum
#         curr_pair_sum = 0
#
#     elif i % 2 != 0 and i >= 1:
#         previous_sum = curr_pair_sum
#         curr_pair_sum = 0
#
# if max_diff == 0:
#     print(f"Yes, value={previous_sum}")
# else:
#     print(f"No, maxdiff={max_diff}")

# -----------------------------------------------------

# pairs_count = int(input())
#
# curr_pair_sum = 0
# previous_sum = 0
# max_diff = 0
#
# for i in range(2 * pairs_count):
#     curr = int(input())
#     curr_pair_sum += curr
#
#     if i % 2 != 0 and i >= 3:
#         max_diff = max(max_diff, abs(curr_pair_sum - previous_sum))
#         previous_sum = curr_pair_sum
#         curr_pair_sum = 0
#
#     elif i % 2 != 0 and i >= 1:
#         previous_sum = curr_pair_sum
#         curr_pair_sum = 0
#
# if max_diff == 0:
#     print(f"Yes, value={previous_sum}")
# else:
#     print(f"No, maxdiff={max_diff}")