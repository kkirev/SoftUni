from math import ceil, floor

days = int(input())
food_left_kg = int(input())
dog_kg_per_day = float(input()) #food in kilos per day
cat_kg_per_day = float(input()) #food in kilos per day
turtle_g_per_day = float(input()) #food in grams per day

dog_consumed = days * dog_kg_per_day
cat_consumed = days * cat_kg_per_day
turtle_consumed = days * turtle_g_per_day / 1000
total_food_consumed = dog_consumed + cat_consumed + turtle_consumed
difference = abs(total_food_consumed - food_left_kg)

if food_left_kg >= total_food_consumed:
    print(f'{floor(difference)} kilos of food left.')
else:
    print(f'{ceil(difference)} more kilos of food are needed.')