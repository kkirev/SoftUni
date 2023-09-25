"""
https://judge.softuni.org/Contests/Compete/Index/2414#2

Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява колко ще е
часът след 15 минути. Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23,
а минутите винаги са между 0 и 59. Часовете се изписват с една или две цифри. Минутите се изписват
винаги с по две цифри, с водеща нула, когато е необходимо.
"""

hours = int(input())
minutes = int(input())

total_minutes = hours * 60 + minutes + 15
hours_output = total_minutes // 60
minutes_output = total_minutes % 60

if hours_output > 23:
    hours_output = 0
if minutes_output <10:
    print(f'{hours_output}:0{minutes_output}')
else:
    print(f'{hours_output}:{minutes_output}')