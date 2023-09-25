"""
https://judge.softuni.org/Contests/Practice/Index/1642#1

Напишете програма, която чете от конзолата страна и височина на триъгълник и пресмята неговото лице. Използвайте
формулата за лице на триъгълник: area = a * h / 2. Форматирате изхода до втория знак след десетичната запетая.
"""

triangle_side = float(input())
triangle_height = float(input())

area = triangle_side * triangle_height / 2

print("%.2f" % area)