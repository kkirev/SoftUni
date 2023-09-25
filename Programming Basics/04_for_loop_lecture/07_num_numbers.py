# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя и ги сумира.
# •	От първия ред на входа се въвежда броят числа n.
# •	От следващите n реда се въвежда по едно цяло число.
# Програмата трябва да прочете числата, да ги сумира и да отпечата сумата им.

numbers_count = int(input())

numbers_sum = 0

for numbers in range(numbers_count):
    current_number = int(input())
    numbers_sum += current_number
print(numbers_sum)