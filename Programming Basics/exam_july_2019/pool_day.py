# Преподавателският екип на СофтУни организира работен ден на басейн по случай настъпването на лятото. Вашата задача е
# да напишете програма, която да изчислява каква сума трябва да се заплати. За всеки един човек от екипа трябва да се
# заплати такса вход. Трябва да имате предвид, че един чадър стига за двама души. Знае се, че само 75% от екипа искат
# шезлонги. При изчислението на броя на чадърите и шезлонгите, техният брой да се закръгли до по-голямото цяло число.

# Вход
# От конзолата се четат 4 числа:
# 1.	Първи ред – брой на хората. Цяло число в интервала [1…100]
# 2.	Втори ред – такса вход. Реално число в интервала [0.00…50.00]
# 3.	Трети ред – цена един за шезлонг. Реално число в интервала [0.00…50.00]
# 4.	Четвърти ред – цена за един чадър. Реално число в интервала [0.00...50.00]

# Изход
# "{сумата за покриване на разходите} lv."
# Резултатът да се форматира до втората цифра след десетичния знак.

import math

count_people = int(input())
entrance_fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

sunbed_needed = math.ceil (count_people * 0.75)
umbrella_needed = math.ceil (count_people / 2)

total_expenses = count_people * entrance_fee + sunbed_needed * sunbed_price + umbrella_needed * umbrella_price

print(f"{total_expenses:.2f} lv.")