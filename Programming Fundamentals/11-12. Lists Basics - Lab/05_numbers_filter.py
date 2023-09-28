"""
On the first line, you will receive a single number n. On the following n lines, you will receive integers.
After that, you will be given one of the following commands:
•	even
•	odd
•	negative
•	positive
Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

Example

Input	    Output
5           [-2, 18, 998]
33
19
-2
18
998
even
"""

integers_numbers = int(input())

even_nums = []
odd_nums = []
negative_nums = []
positive_nums = []

for integer in range(integers_numbers):
    current_integer = int(input())

    if current_integer < 0:
        negative_nums.append(current_integer)
    else:
        positive_nums.append(current_integer)

    if current_integer % 2 == 0:
        even_nums.append(current_integer)
    else:
        odd_nums.append(current_integer)

command = input()

if command == "even":
    print(even_nums)
elif command == "odd":
    print(odd_nums)
elif command == "negative":
    print(negative_nums)
elif command == "positive":
    print(positive_nums)