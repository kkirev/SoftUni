people_count = int(input())
nights_count = int(input())
transport_pass_count = int(input())
museum_pass_count: int = int(input())

total_sum = people_count * (nights_count * 20 + transport_pass_count * 1.6 + museum_pass_count * 6) * 1.25


print(f'{total_sum: .2f}')
