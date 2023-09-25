"""
Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky. Create a program that receives
a person's age and prints what he/she drinks.

Rules:
A kid is defined as someone under or at the age of 14.
A teen is defined as someone under or at the age of 18.
A young adult is defined as someone under or at the age of 21.
An adult is defined as someone above the age of 21.
Note: All the values are inclusive except the last one!
"""

age_person = int(input())

drink = ''
if age_person <= 14:
    drink = 'drink toddy'
elif age_person <= 18:
    drink = 'drink coke'
elif age_person <= 21:
    drink = 'drink beer'
else:
    drink = 'drink whisky'

print(drink)