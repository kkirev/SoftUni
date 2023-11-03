"""
You are saying goodbye to your best friend: "See you next happy year". Happy Year is the year with only distinct digits,
for example, 2018. Write a program that receives an integer number and finds the next happy year.

    Examples:
Input       Output
8989        9012
1001        1023
"""

year = int(input())
year_is_special = False
while not year_is_special:
    year += 1
    year_as_string = str(year)
    year_is_special = True
    for digit in year_as_string:
        if year_as_string.count(digit) > 1:
            year_is_special = False
            break
print(year)