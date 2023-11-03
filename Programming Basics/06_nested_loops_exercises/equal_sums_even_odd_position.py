"""
Напишете програма, която чете от конзолата две шестцифрени цели числа. Винаги първото въведено число ще бъде по-малко
от второто. На конзолата да се отпечатат на 1, ред разделени с интервал, всички числа, които се намират между двете,
прочетени от конзолата числа и отговарят на условието сумата от цифрите на четни и нечетни позиции да са равни.
Ако няма числа, отговарящи на условието на конзолата не се извежда резултат.
"""

num1 = int(input())
num2 = int(input())

for number in range (num1, num2 + 1):
    even_sum = 0
    odd_sum = 0
    num_to_str = str(number)

    for index in range(len(num_to_str)):
        if index % 2 != 0:
            odd_sum += int(num_to_str[index])
        else:
            even_sum += int(num_to_str[index])
    if odd_sum == even_sum:
        print(number, end=' ')

# -----------------------------------------------------------

# num1 = int(input())
# num2 = int(input())
#
# for number in range (num1, num2 + 1):
#     even_sum = 0
#     odd_sum = 0
#     num_to_str = str(number)
#
#     for index, digit in enumerate(num_to_str):
#         if index % 2 != 0:
#             odd_sum += int(digit)
#         else:
#             even_sum += int(digit)
#     if odd_sum == even_sum:
#         print(number, end=' ')