days_count = int(input())
accomm_type = input()
feedback = input()

night_price = 0

if accomm_type == 'room for one person':
    night_price = 18
elif accomm_type == 'apartment':
    night_price = 25
    if days_count < 10:
        night_price *= 0.7
    elif 10 <= days_count <= 15:
        night_price *= 0.65
    else:
        night_price *= 0.5
elif accomm_type == 'president apartment':
    night_price = 35
    if days_count < 10:
        night_price *= 0.9
    elif 10 <= days_count <= 15:
        night_price *= 0.85
    else:
        night_price *= 0.8

final_sum = (days_count - 1) * night_price

if feedback == 'positive':
    final_sum *= 1.25
elif feedback == 'negative':
    final_sum *= 0.9


print(f'{final_sum:.2f}')