"""
You are a facility manager at a large business center. One of your responsibilities is to check if each conference room
in the center has enough chairs for the visitors.

On the first line, you will be given an integer n representing the number of rooms in the business center.
On the following n lines for each room, you will receive information about the chairs in the room and the number of
visitors. Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors
at the end. For example: "XXXXX 4" (5 chairs and 4 visitors).

Keep track of the free chairs:
•	If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs
needed in room {number_of_room}". The rooms start from 1.
•	Otherwise, print: "Game On, {total_free_chairs} free chairs left".
"""

rooms_count = int(input())
extra_chairs = 0
room_counter = 0
chairs_for_everyone = True

for room in range(rooms_count):
	room_counter += 1
	chairs_count, visitors_count = input().split()
	chairs_count = len(chairs_count)
	visitors_count = int(visitors_count)

	if chairs_count >= visitors_count:
		extra_chairs += (chairs_count - visitors_count)
	else:
		chairs_for_everyone = False
		print(f"{visitors_count - chairs_count} more chairs needed in room {room_counter}")

if chairs_for_everyone:
	print(f"Game On, {extra_chairs} free chairs left")

# --------------------------------------------------------------------------------------------------------------------
#
#
# def check_the_rooms(number_of_rooms):
# 	free_chairs = 0
# 	for number_of_room in range(1, number_of_rooms + 1):
# 		free_chairs_in_current_room, visitors = input().split()
# 		difference = len(free_chairs_in_current_room) - int(visitors)
# 		if difference < 0:
# 			print(f"{abs(difference)} more chairs needed in room {number_of_room}")
# 		free_chairs += difference
# 	return free_chairs
#
#
# count_of_rooms = int(input())
# total_free_chairs = check_the_rooms(count_of_rooms)
# if total_free_chairs >= 0:
# 	print(f"Game On, {total_free_chairs} free chairs left")