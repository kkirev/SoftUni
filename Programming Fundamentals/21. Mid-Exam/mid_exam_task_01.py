experience_amount_target = float(input())
battles_count = int(input())

player_experience = 0
battle_counter = 0

job_done = False

for battle in range(1, battles_count + 1):
	battle_experience = float(input())
	player_experience += battle_experience
	battle_counter += 1

	if battle_counter % 3 == 0:
		player_experience += battle_experience * 0.15

	if battle_counter % 5 == 0:
		player_experience -= battle_experience * 0.1

	if battle_counter % 15 == 0:
		player_experience += battle_experience * 0.05

	if player_experience >= experience_amount_target:
		job_done = True
		break

if job_done:
	print(f"Player successfully collected his needed experience for {battle_counter} battles.")
else:
	difference = abs(experience_amount_target - player_experience)
	print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")
