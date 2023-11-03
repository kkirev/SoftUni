holidays = int(input())

year_play_limit = 30000    #Tom's play norm in minutes for a year
working_days_play = (365 - holidays) * 63    #Total play time in working days
holidays_play = holidays * 127    #Total play time in holidays
total_play_time = working_days_play + holidays_play    #Total play time for a year
difference_hours = abs(year_play_limit - total_play_time) // 60
difference_minutes = abs(year_play_limit - total_play_time) % 60

if year_play_limit < total_play_time:
    print('Tom will run away')
    print(f'{difference_hours:.0f} hours and {difference_minutes:.0f} minutes more for play')
elif year_play_limit >= total_play_time:
    print('Tom sleeps well')
    print(f'{difference_hours} hours and {difference_minutes} minutes less for play')