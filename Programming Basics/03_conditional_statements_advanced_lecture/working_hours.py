time = int(input())
day_of_week = input().lower()

if day_of_week == "monday" or day_of_week == "tuesday" or day_of_week == "wednesday" or day_of_week == "thursday" \
        or day_of_week == "friday" or day_of_week == "saturday":
    if 10 <= time <= 18:
        print("open")
    else:
        print("closed")
elif day_of_week == "sunday":
    print("closed")

#hour = int(input())
#day = input()
#work_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#weekend = ['Saturday', 'Sunday']
#
#if day in work_day:
#    if 10 < hour < 18:
#        print('open')
#    else:
#        print('closed')
#elif day in weekend:
#    print('closed')