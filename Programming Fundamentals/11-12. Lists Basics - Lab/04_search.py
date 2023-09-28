"""
On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines,
you will be given some strings. You should add them to a list and print them. After that, you should filter out only
the strings that include the given word and print that list too.

Example

Input	                                Output
3                                       ["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]
SoftUni                                 ["I study at SoftUni", "I learn Python at SoftUni"]
I study at SoftUni
I walk to work
I learn Python at SoftUni
"""

strings_number = int(input())
word = input()

all_strings = []
selected_strings = []

for string in range(strings_number):
    current_string = input()
    all_strings.append(current_string)

    if word in current_string:
        selected_strings.append(current_string)

print(all_strings)
print(selected_strings)
