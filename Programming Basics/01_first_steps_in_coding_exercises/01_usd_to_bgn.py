"""
https://judge.softuni.org/Contests/Compete/Index/2424#0

Напишете програма за конвертиране на щатски долари (USD) в български лева (BGN).
Използвайте фиксиран курс между долар и лев: 1 USD = 1.79549 BGN.
"""

usd = float(input())
bgn = usd * 1.79549

print(bgn)