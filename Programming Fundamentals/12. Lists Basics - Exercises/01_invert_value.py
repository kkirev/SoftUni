"""
Write a program that receives a single string containing positive and negative numbers separated by a single space.
Print a list containing the opposite of each number.

Example:

Input	                Output
1 2 -3 -3 5	            [-1, -2, 3, 3, -5]
-4 0 2 57 -101	        [4, 0, -2, -57, 101]
"""

string_to_list = input().split()
opposite_list = []

for element in string_to_list:
    num = int(element)
    opposite_list.append(-num)

print(opposite_list)
