"""
You will be given strings until you receive the command "End". For each string given, you should print a string in
which each character (case-sensitive) is repeated twice. Note that if you receive the string "SoftUni",
you should NOT print it!
"""

given_string = input()

while given_string != "End":
    if given_string != 'SoftUni':
        doubled_string = ''

        for character in given_string:
            doubled_string += character * 2
        print(doubled_string)
    given_string = input()

#--------------------------------------------------------------------

# while True:
#     given_string = input()
#
#     if given_string == "End":
#         break
#
#     if given_string != "SoftUni":
#         doubled_string = ''.join(char * 2 for char in given_string)
#         print(doubled_string)
