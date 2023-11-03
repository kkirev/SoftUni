start_points = 301
multiplier = 0
current_points = 0
successful_shots = 0
unsuccessful_shots = 0
is_retiring = False
is_winning = False

player_name = input()
while True:
    shot_factor = input()
    if shot_factor == 'Retire':
        is_retiring = True
        break
    elif shot_factor == 'Single':
        multiplier = 1
    elif shot_factor == 'Double':
        multiplier = 2
    elif shot_factor == 'Triple':
        multiplier = 3

    shot_points = int(input())

    current_points = multiplier * shot_points

    if start_points - current_points > 0:
        successful_shots += 1
        start_points -= current_points
    elif start_points - current_points < 0:
        current_points = 0
        unsuccessful_shots += 1
    elif start_points - current_points == 0:
        successful_shots += 1
        is_winning = True
        break

if is_winning:
    print(f'{player_name} won the leg with {successful_shots} shots.')
if is_retiring:
    print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')