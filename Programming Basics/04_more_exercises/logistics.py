"""
https://judge.softuni.org/Contests/Practice/Index/1680#0

Отговаряте за логистиката на различни товари. В зависимост от теглото на товара е нужно различно превозно средство.
Цената на тон, за която се превозва товара е различна за всяко превозно средство:
•	До 3 тона – микробус (200 лева на тон)
•	От 4 до 11 тона – камион (175 лева на тон)
•	12 и повече тона – влак (120 лева на тон)
Вашата задача е да изчислите средната цена на тон превозен товар, както и процента на тоновете  превозвани с

всяко превозно средство, спрямо общото тегло(в тонове) на всички товари.
Вход
От конзолата се четат поредица от числа, всяко на отделен ред:
•	На първия ред – броя на товарите за превоз – цяло число в интервала [1...1000]
•	За всеки един товар на отделен ред – тонажа на товара – цяло число в интервала [1...1000]

Изход
Да се отпечатат на конзолата 4 реда, както следва:
•	Първи ред – средната цена на тон превозен товар (закръглена до втория знак след дес. запетая);
•	Втори ред – процентът тона превозвани с микробус (процент между 0.00% и 100.00%);
•	Трети ред – процентът  тона превозвани с камион (процент между 0.00% и 100.00%);
•	Четвърти ред – процентът тона превозвани с влак (процент между 0.00% и 100.00%).
"""
# User input
cargo_count = int(input())

# Variables
price_per_ton = 0
total_mass = 0
total_price = 0
bus_total_mass = 0
truck_total_mass = 0
train_total_mass = 0

# Logic
for cargo in range(cargo_count):
    cargo_mass = int(input())
    if cargo_mass <= 3:
        price_per_ton = 200
        total_price += cargo_mass * price_per_ton
        total_mass += cargo_mass
        bus_total_mass += cargo_mass
    elif 3 < cargo_mass <= 11:
        price_per_ton = 175
        total_price += cargo_mass * price_per_ton
        total_mass += cargo_mass
        truck_total_mass += cargo_mass
    else:
        price_per_ton = 120
        total_price += cargo_mass * price_per_ton
        total_mass += cargo_mass
        train_total_mass += cargo_mass

average_price_per_ton = total_price / total_mass
percent_mass_by_bus = bus_total_mass / total_mass * 100
percent_mass_by_truck = truck_total_mass / total_mass * 100
percent_mass_by_train = train_total_mass / total_mass * 100

# Output
print(f'{average_price_per_ton:.2f}')
print(f'{percent_mass_by_bus:.2f}%')
print(f'{percent_mass_by_truck:.2f}%')
print(f'{percent_mass_by_train:.2f}%')