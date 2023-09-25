"""
https://judge.softuni.org/Contests/Practice/Index/1642#7

Напишете програма, която чете от конзолата число r и пресмята и отпечатва лицето и периметъра на кръг / окръжност с
радиус r, като форматирате изхода в следния вид: "<calculated area>"
"<calculated parameter>". Форматирайте изходните данни до втория знак след десетичната запетая.
"""

from math import pi

r = float(input())

circle_area = pi * r ** 2
circle_perimeter = 2 * pi * r

print(f"{circle_area:.2f}")
print(f"{circle_perimeter:.2f}")