"""
https://judge.softuni.org/Contests/Practice/Index/1642#8

Напишете програма, която познава дали е топло или студено навън. От конзолата се чете един ред – текст, който подсказва
какво е времето. При въвеждане на "sunny" трябва да се отпечата "It's warm outside!".
Във всички останали случаи трябва да се отпечата "It's cold outside!".
"""

weather = str(input())
if weather == "sunny":
    print("It's warm outside!")
else:
    print("It's cold outside!")