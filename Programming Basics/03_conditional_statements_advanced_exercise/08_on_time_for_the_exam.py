exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minuets = int(input())

total_exam_mins = exam_hours * 60 + exam_minutes
total_arrival_mins = arrival_hours * 60 + arrival_minuets
difference = abs(total_arrival_mins - total_exam_mins)

if total_arrival_mins == total_exam_mins:
    print('On time')
elif total_arrival_mins < total_exam_mins and difference <= 30:
    print('On time')
    print(f'{difference} minutes before the start')
elif total_arrival_mins < total_exam_mins and 30 < difference < 60:
    print('Early')
    print(f'{difference} minutes before the start')
elif total_arrival_mins < total_exam_mins and difference >= 60:
    print('Early')
    print(f'{difference // 60}:{difference % 60:02d} hours before the start')
elif total_arrival_mins > total_exam_mins and difference < 60:
    print('Late')
    print(f'{difference} minutes after the start')
elif total_arrival_mins > total_exam_mins and difference >= 60:
    print('Late')
    print(f'{difference // 60}:{difference % 60:02d} hours after the start')