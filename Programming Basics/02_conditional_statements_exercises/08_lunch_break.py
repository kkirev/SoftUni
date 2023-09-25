"""
https://judge.softuni.org/Contests/Compete/Index/2414#7

По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да напишете програма,
с която ще разберете дали имате достатъчно време да изгледате епизода. По време на почивката отделяте време за обяд и
време за отдих. Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.

Вход
От конзолата се четат 3 реда:
1.	Име на сериал – текст
2.	Продължителност на епизод  – цяло число в диапазона [10… 90]
3.	Продължителност на почивката  – цяло число в диапазона [10… 120]

Изход
На конзолата да се изпише един ред:
•	Ако времето е достатъчно да изгледате епизода:
"You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
•	Ако времето не Ви е достатъчно:
"You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
Времето да се закръгли до най-близкото цяло число нагоре.
"""
from math import ceil

series_name = input()
episode_length = int(input())
break_length = int(input())

lunch_time = 1/8 * break_length
rest_time = 1/4 * break_length
remaining_time = break_length - lunch_time -rest_time
time_gap = abs(episode_length - remaining_time)

if remaining_time >= episode_length:
    print(f'You have enough time to watch {series_name} and left with {ceil(time_gap)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(time_gap)} more minutes.")