# https://judge.softuni.org/Contests/2419

# Напишете програма, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход.
# •	при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола.
# •	при въвеждане на правилна парола: отпечатваме "Welcome {username}!".

username = input()
password = input()

user_input = input()
while user_input != password:
    user_input = input()
print(f'Welcome {username}!')