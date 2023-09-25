"""
Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:

Examples:

Input       Output      Input       Output
3           aaa            2        aaa
aab                                 aba
aac                                 abb
aba                                 baa
abb                                 baa
abc                                 bab
aca                                 bba
acb                                 bbb
acc
baa
bab
bac
bba
bbb
bbc
bca
bcb
bcc
caa
cab
cac
cba
cbb
cbc
cca
ccb
ccc
"""

symbols_count = int(input())
for first_symbol in range(symbols_count):
    for second_symbol in range(symbols_count):
        for third_symbol in range(symbols_count):
            print(chr(first_symbol + 97) + chr(second_symbol + 97) + chr(third_symbol + 97))