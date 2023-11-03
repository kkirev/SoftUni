"""
Write a program that announces the winner of a car race.
You will receive a sequence of numbers. Each number represents the time the car needs to pass through that
step (the index). There will be two cars. The first one starts from the left side, and the other one starts from the
right side. The middle index of the sequence is the finish line.
Calculate the total time each racer needs to reach the finish line and print the winner with his total
time (the racer with less time). If you have a zero in the list, you should reduce the racer's time that
reached it by 20% (from his current time).
The number of elements in the sequence will always be odd.
Print the result in the following format "The winner is {left/right} with total time: {total_time}".
The time should be formatted to the first decimal point.

Example:

Input										Output
29 13 9 0 13 0 21 0 14 82 12				The winner is left with total time: 53.8

Input										Output
123 20 4 0 13 0 0 5 5 14 0					The winner is right with total time: 19.2
"""

checkpoints = input().split()

left_time = 0
right_time = 0
index = 0

for time_index in range(len(checkpoints) // 2):
	left_time += int(checkpoints[time_index])
	if int(checkpoints[time_index]) == 0:
		left_time *= 0.8

for time_index in range(len(checkpoints) - 1, len(checkpoints) // 2, -1):
	right_time += int(checkpoints[time_index])
	if int(checkpoints[time_index]) == 0:
		right_time *= 0.8

if left_time < right_time:
	print(f"The winner is left with total time: {left_time:.1f}")
else:
	print(f"The winner is right with total time: {right_time:.1f}")



