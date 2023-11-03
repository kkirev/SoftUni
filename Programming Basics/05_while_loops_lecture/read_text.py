# https://judge.softuni.org/Contests/2419

# Напишете програма, която чете текст от конзолата(стринг) и го принтира, докато не получи командата "Stop".

user_input = input()
while user_input != 'Stop':
    print(user_input)
    user_input = input()


# while True:
#     user_input = input()
#     if user_input == 'Stop':
#         break
#     print(user_input)