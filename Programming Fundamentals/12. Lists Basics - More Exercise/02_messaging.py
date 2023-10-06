"""
On the first line, you will receive a sequence of numbers separated by a single space. On the second line, you will
receive a string.
Your task is to write a program that sends a message only using chars from the given string. Each char the program
adds to the message should be found by its index. The index you are looking for is the sum of a number's digits from
the first sequence. If the index is greater than the length of the text, continue counting from the beginning \
(so that you always have a valid index). When you find a char, you should add it to the message and remove it from
the string. It means that for the following index, the text will contain one character less.
Print the final message.

Example:

Input                                   Output

9992 562 8933                           hey
This is some message for you

2 122 1123 1321 9 17211                 judge!
87j973u59dg37e725!
"""

numbers = input().split()
string = list(input())
message = []

for num in numbers:
    digit_sum = 0
    for digit in str(num):
        digit_sum += int(digit)
    while digit_sum >= len(string):
        digit_sum -= len(string)
    if string[digit_sum] in string:
        message.append(string[digit_sum])
        string.pop(digit_sum)

print("".join(message))

#  Judge result - 100/100