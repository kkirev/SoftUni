"""
Write a program that receives a list of integer numbers (separated by a single space) and a number n.
The number n represents the count of numbers to remove from the list. You should remove the smallest ones,
and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".

Example:

Input                   Output
10 9 8 7 6 5            10, 9, 8
3

Input                   Output
1 10 2 9 3 8            10, 9, 3, 8
2
"""

user_input = input().split()
removed_numbers_count = int(input())

list_of_integers = []
for element in range(len(user_input)):
    user_input[element] = int(user_input[element])
    list_of_integers.append(user_input[element])

for number in range(removed_numbers_count):
    list_of_integers.remove(min(list_of_integers))

list_of_strings = []
for integer in list_of_integers:
    list_of_strings.append(str(integer))

print(", ".join(list_of_strings))