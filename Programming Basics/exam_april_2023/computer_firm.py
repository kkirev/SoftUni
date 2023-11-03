computers_count = int(input())

average_pc_rate = 0
forcast_sales = 0
real_sales = 0
total_sales = 0
total_rating = 0

for pc in range(computers_count):
    complex_info = int(input())
    average_pc_rate = complex_info % 10
    forcast_sales = complex_info // 10
    total_rating += average_pc_rate

    if average_pc_rate == 2:
        real_sales = 0
    elif average_pc_rate == 3:
        real_sales = forcast_sales * 0.5
    elif average_pc_rate == 4:
        real_sales = forcast_sales * 0.7
    elif average_pc_rate == 5:
        real_sales = forcast_sales * 0.85
    elif average_pc_rate == 6:
        real_sales = forcast_sales

    total_sales += real_sales
total_rating /= computers_count

print(f'{total_sales:.2f}')
print(f'{total_rating:.2f}')
