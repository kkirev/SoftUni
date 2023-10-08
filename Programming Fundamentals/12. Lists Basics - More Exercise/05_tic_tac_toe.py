"""
You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.

Legend:
•	0 - empty space
•	1 - first player move
•	2 - second player move

Find out who the winner is. If the first player wins, print "First player won". If the second player wins,
print "Second player won". Otherwise, print "Draw!".
"""

line_1 = input().split()
line_2 = input().split()
line_3 = input().split()

winner = ''
player = ''

for player in range(1, 3):
	player = str(player)
	winning_line = [player, player, player]

	if line_1 == winning_line or line_2 == winning_line or line_3 == winning_line: # Checking the all rows
		winner = player

	elif line_1[0] == player and line_2[0] == player and line_3[0] == player: # Checking the first column
		winner = player
	elif line_1[1] == player and line_2[1] == player and line_3[1] == player: # Checking the second column
		winner = player
	elif line_1[1] == player and line_2[1] == player and line_3[1] == player: # Checking the third column
		winner = player

	elif line_1[0] == player and line_2[1] == player and line_3[2] == player: # Checking the first diagonal
		winner = player
	elif line_1[2] == player and line_2[1] == player and line_3[0] == player: # Checking the second diagonal
		winner = player

if winner == str(1):
	print("First player won")
elif winner == str(2):
	print("Second player won")
else:
	print("Draw!")
