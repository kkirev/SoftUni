chrysanthemums_count = int(input()) #Брой закупени хризантеми
roses_count = int(input()) #Брой закупени рози
tulips_count = int(input()) #Брой закупени лалета
season = input() #Един от четирите сезона
holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
bouquet_price = 0

if season == 'Spring' or season == 'Summer':
    chrysanthemums_price = 2
    roses_price = 4.1
    tulips_price = 2.5
elif season == 'Autumn' or season == 'Winter':
    chrysanthemums_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15

bouquet_price = chrysanthemums_count * chrysanthemums_price + roses_count * roses_price + \
                tulips_count * tulips_price

if holiday == 'Y':
    bouquet_price *= 1.15

if season == 'Spring' and tulips_count > 7:
    bouquet_price *= 0.95
elif season == 'Winter' and roses_count >= 10:
    bouquet_price *= 0.9

if chrysanthemums_count + roses_count + tulips_count > 20:
    bouquet_price *= 0.8

print(f'{bouquet_price + 2:.2f}')