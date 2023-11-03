# https://judge.softuni.org/Contests/2419

# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-голямото измежду тях и го принтира. Въвежда се по едно число на ред.

user_input = input()
max_number = int(user_input)

while user_input != 'Stop':
    user_input = int(user_input)

    if user_input > max_number:
        max_number = user_input

    user_input = input()

print(max_number)