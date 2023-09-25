"""
You will be given an integer that represents a distance in meters. Write a program that converts meters to kilometers
formatted to the second decimal point
"""

distance_in_meters = float(input())
distance_in_kilometers = distance_in_meters / 1000

print(f"{distance_in_kilometers:.2f}")