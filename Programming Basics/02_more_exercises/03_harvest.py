from math import floor, ceil

vineyard = int(input()) #The whole area of the vineyard in square meters
grape_per_sq_m = float(input()) #Grapes amount in kilos per square meter
wine_liters_needed = int(input()) #Amount of wine needed in liters
num_of_workers = int(input()) #Numbers of workers

production_area = vineyard * 0.4 #40% from the whole area is used for wine production
wine_litters_produced = production_area * grape_per_sq_m / 2.5 #2.5 liters wine are produce from one square meter
difference =  abs(wine_litters_produced - wine_liters_needed)

if wine_litters_produced < wine_liters_needed:
    print(f'It will be a tough winter! More {floor(difference)} liters wine needed.')
elif wine_litters_produced >= wine_liters_needed:
    print(f'Good harvest this year! Total wine: {floor(wine_litters_produced)} liters.')
    print(f'{ceil(difference)} liters left -> {ceil(difference / num_of_workers)} liters per person.')