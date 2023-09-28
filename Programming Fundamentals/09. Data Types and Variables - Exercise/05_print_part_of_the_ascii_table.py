"""
Write a program that prints part of the ASCII table characters on the console, separated by a single space.
On the first line of input, you will receive the char index you should start with.
On the second line - the index of the last character you should print.

Input               Output
60                  < = > ? @ A
65

69                  E F G H I J K L M N O
79

97                 a b c d e f g h
104
"""

start_char = int(input())
end_char = int(input())

for char in range(start_char, end_char + 1):
    print(chr(char), end=' ')