"""
https://judge.softuni.org/Contests/Practice/Index/1642#9

Напишете програма, която при въведени градуси (реално число) принтира какво е времето,
като имате предвид следната таблица:

    Градуси	        Време
26.00 - 35.00	    Hot
20.1 - 25.9	        Warm
15.00 - 20.00	    Mild
12.00 - 14.9	    Cool
5.00 - 11.9	        Cold

Ако се въведат градуси, различни от посочените в таблицата, да се отпечата "unknown".
"""

temp = float(input())
if 26.00 <= temp <= 35.00:
    print("Hot")
elif 20.1 <= temp <= 25.9:
    print("Warm")
elif 15.00 <= temp <= 20.00:
    print("Mild")
elif 12.00 <= temp <= 14.9:
    print("Cool")
elif 5.00 <= temp <= 11.9:
    print("Cold")
else:
    print("unknown")