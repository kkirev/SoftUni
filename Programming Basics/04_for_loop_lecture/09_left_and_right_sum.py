# Да се напише програма, която чете 2 * n-на брой цели числа, подадени от потребителя и проверява дали сумата
# на първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума).
# При равенство печата "Yes, sum = " + сумата; иначе печата "No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).

numbers_count = int(input())

sum_left = 0
sum_right = 0

for numbers in range(numbers_count * 2):
    current_num = int(input())
    if numbers < numbers_count:
        sum_left += current_num
    else:
        sum_right += current_num

if sum_left == sum_right:
     print(f'Yes, sum = {sum_left}')
else:
    print(f'No, diff = {abs(sum_left - sum_right)}')

#---------------------------------------------------------
# numbers_count = int(input())
#
# sum_left = 0
# sum_right = 0
#
# for numbers in range(numbers_count):
#     current_num = int(input())
#     sum_left += current_num
#
# for numbers in range(numbers_count):
#     current_num = int(input())
#     sum_right += current_num
#
# if sum_left == sum_right:
#     print(f'Yes, sum = {sum_left}')
# else:
#     print(f'No, diff = {abs(sum_left - sum_right)}')
#---------------------------------------------------------
