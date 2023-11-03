"""
Peter is a programming enthusiast who wants to create a chat where people will send messages via number codes.
He starts by creating a program for only four messages.
Create a program that receives the n number of messages sent. On the following n lines, it will receive integer numbers.
For each number, the program should print a different message:

•	If the number is 88 - "Hello"
•	If the number is 86 - "How are you?"
•	If the number is not 88 nor 86, and it is below 88 - "GREAT!"
•	If the number is over 88 - "Bye."
"""

messages_count = int(input())

for message in range(messages_count):
    current_message = int(input())

    if current_message == 88:
        print('Hello')
    elif current_message == 86:
        print('How are you?')
    elif current_message == 87 or current_message < 86:
        print('GREAT!')
    else:
        print('Bye.')
