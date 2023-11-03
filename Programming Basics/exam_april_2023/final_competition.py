dancers_count = int(input())
points_count = float(input())
season = input()
competition_place = input()

money_prize = 0

if competition_place == 'Bulgaria':
    money_prize = points_count * dancers_count
    if season == 'summer':
        money_prize *= 0.95
    elif season == 'winter':
        money_prize *= 0.92

elif competition_place == 'Abroad':
    money_prize = points_count * dancers_count * 1.5
    if season == 'summer':
        money_prize *= 0.90
    elif season == 'winter':
        money_prize *= 0.85

charity_sum = money_prize * 0.75
sum_left = money_prize - charity_sum
sum_per_dancer = sum_left / dancers_count

print(f'Charity - {charity_sum:.2f}')
print(f'Money per dancer - {sum_per_dancer:.2f}')