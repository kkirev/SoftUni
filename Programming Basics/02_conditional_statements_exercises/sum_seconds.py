"""
https://judge.softuni.org/Contests/Compete/Index/2414#0

Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50). Да се напише програма, която чете времената
на състезателите в секунди, въведени от потребителя и пресмята сумарното им време във формат "минути:секунди".
Секундите да се изведат с водеща нула (2  "02", 7  "07", 35  "35").

вход	изход		    вход	изход		    вход	изход		    вход	изход
	        		    22                      50                      14
                        7                       50                      12
        2:04            34	    1:03		    49      2:29		    10      0:36
"""

time_first = int(input())
time_second = int(input())
time_third = int(input())

time_in_minutes = (time_first + time_second + time_third) // 60
time_in_seconds = (time_first + time_second + time_third) % 60

if time_in_seconds < 10:
    print(f'{time_in_minutes}:0{time_in_seconds}')
else:
    print(f'{time_in_minutes}:{time_in_seconds}')
