"""
You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the number of lines,
which will follow. On the following n lines, you will receive liters of water (integers), which you should pour into
your tank. If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line.
On the last line, print the liters in the tank.
"""

line_numbers = int(input())
tank_capacity = 255
loaded_amount = 0

for line in range(line_numbers):
    current_amount = int(input())
    loaded_amount += current_amount
    if current_amount > tank_capacity:
        print(f"Insufficient capacity!" )
        current_amount = int(input())
        
