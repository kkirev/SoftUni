"""
Write a program that receives two numbers (factor and count). It should create a list with a length of the given count
that contains only integer numbers, which are multiples of the given factor. The numbers should be only positive,
and they should be arranged in ascending order, starting from the value of the factor.

Example:

Input	      |      Output
------------------------------------------------------
2             |     [2, 4, 6, 8, 10]
5             |
--------------|--------------------------------------
1             |     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
10            |
"""

# factor_num = int(input())
# count_num = int(input())
#
# result_list = []
#
# for num in range(count_num):
#     result_list.append(factor_num + (num * factor_num))
#
# print(result_list)
# ------------------------------------------------------------------
factor_num = int(input())
count_num = int(input())

result_list = []

for num in range(1, count_num + 1):
    result_list.append((factor_num * num)

print(result_list)