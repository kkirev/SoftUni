"""
Write a program, which sums the ASCII codes of N characters and prints the sum on the console. On the first line,
you will receive N – the number of lines. On the following N lines – you will receive a letter per line.
Print the total sum in the following format: "The sum equals: {total_sum}".

Note: n will be in the interval [1…20].
"""

chars_number = int(input())
ascii_sum = 0

for char in range(chars_number):
    letter = input()
    ascii_sum += ord(letter)

print(f"The sum equals: {ascii_sum}")