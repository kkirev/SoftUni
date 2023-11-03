distance_km = int(input())
part_of_the_day = input()
taxi_day_rate = 0.79
taxi_night_rate = 0.9
bus_rate = 0.09
train_rate = 0.06
best_price = 0

if distance_km < 20:
    if part_of_the_day == "day":
        best_price = 0.70 + (distance_km * taxi_day_rate)
    else:
        best_price = 0.70 + (distance_km * taxi_night_rate)
elif distance_km >= 100:
    best_price = distance_km * train_rate
else:
    best_price = distance_km * bus_rate

print(f'{best_price:.2f}')