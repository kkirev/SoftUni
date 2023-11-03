"""
Write a program that receives three whole numbers and prints the largest one.
"""

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_1 > num_2 and num_1 > num_3:
    print(num_1)
elif num_2 > num_1 and num_2 > num_3:
    print(num_2)
elif num_3 > num_1 and num_3 > num_2:
    print(num_3)


# num1, num2, num3 = int(input()), int(input()), int(input())
# largest = max(num1, num2, num3)
# print(largest)