"""
https://judge.softuni.org/Contests/Practice/Index/1680#0

Напишете програма която да пресмята средният разход за месец на семейство за даден период време.
За всеки месец разходите са следните:
•	За ток – всеки месец е различен, ще се чете от конзолата
•	за вода – 20 лв.
•	за интернет – 15 лв.
•	за други – събират се тока, водата и интернета за месеца и към сумата се прибавят 20%.
За всеки разход трябва да се пресметне колко общо е платено за всички месеци.
Вход
Входът се чете от конзолата:
•	Първи ред – месеците за които се търси средният разход – цяло число в интервала [1...100]
•	За всеки месец – сметката за ток – реално число в интервала [1.00...1000.00]
Изход
Да се отпечата на конзолата 5 реда:
•	1ви ред: "Electricity: {ток за всички месеци} lv"
•	2ри ред: "Water: {вода за всички месеци} lv"
•	3ти ред: "Internet: {интернет за всички месеци} lv"
•	4ти ред: "Other: {други за всички месеци} lv"
•	5ти ред: "Average: {средно всички разходи за месец} lv"
Всички числа трябва да са форматирана до вторият знак след запетаята.
"""

# User input
months_count = int(input())

electricity_total = 0
water_total = 0
internet_total = 0
others_total = 0

# Logic
for month in range(months_count):
    electricity_bill = float(input())
    water_bill = 20
    internet_bill = 15
    others_bill = (electricity_bill + water_bill + internet_bill) * 1.2
    electricity_total += electricity_bill
    water_total += water_bill
    internet_total += internet_bill
    others_total += others_bill

average_bill = (electricity_total + water_total + internet_total + others_total) / months_count

# Output
print(f'Electricity: {electricity_total:.2f} lv')
print(f'Water: {water_total:.2f} lv')
print(f'Internet: {internet_total:.2f} lv')
print(f'Other: {others_total:.2f} lv')
print(f'Average: {average_bill:.2f} lv')