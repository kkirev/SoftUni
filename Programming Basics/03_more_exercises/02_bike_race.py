juniors_count = int(input())
seniors_count = int(input())
track_type = input()

senior_donation = 0
junior_donation = 0

if track_type == 'trail':
    junior_donation = 5.50
    senior_donation = 7
elif track_type == 'cross-country':
    junior_donation = 8
    senior_donation = 9.50
    if seniors_count + juniors_count >= 50:
        junior_donation *= 0.75
        senior_donation *= 0.75
elif track_type == 'downhill':
    junior_donation = 12.25
    senior_donation = 13.75
elif track_type == 'road':
    junior_donation = 20
    senior_donation = 21.50

total_income = (seniors_count * senior_donation + juniors_count * junior_donation) * 0.95

print(f'{total_income:.2f}')
