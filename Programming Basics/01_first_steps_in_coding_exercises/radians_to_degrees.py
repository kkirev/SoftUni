"""
https://judge.softuni.org/Contests/Compete/Index/2424#1

Напишете програма, която чете ъгъл в радиани (десетично число) и го преобразува в градуси. Използвайте формулата:
градус = радиан * 180 / π. Числото π в Python може да достъпите чрез модула math.
а да ползвате функционалността му, първо трябва да включите констатата pi.
"""

from math import pi
radians = float(input())
degrees = radians * 180 / pi

print(degrees)