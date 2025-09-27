# Using a 7x7 grid so max Connect7
from typing import Literal

grid: list[list[int]] = [[0 for _ in range(7)] for _ in range(7)]

def add_to_column(column: int, player: Literal[-1, 1]) -> list[list[int]]:
	global grid
	if grid[0][column] != 0:
		raise IndexError("Column taken up")
	for i in range(1, 7):
		if grid[0][i] != 0:
			grid[0][i-1] = player
	return grid

def check_if_won(grid: list[list[int]], x: Literal[2,3,4,5,6,7]) -> int:
	# Returns 0 means no one won. Returning 1 or -1 means that player won

	# Checks vertical
	for j in range(7):
		counter = 0
		player = 0
		for i in range(7-x):
			if grid[i][j] != 0 and player = 0:
				player = grid[i][j]
				counter += 1
			elif grid[i][j] != 0 and grid[i][j] == player:
				counter += 1
			elif grid[i][j] == 0 and player != 0:
				counter = 0
				player = 0

			if counter == x:
				return player

	# Checks horizontal
	for i in range(7):
		counter = 0
		player = 0
		for j in range(7-x):
			if grid[i][j] != 0 and player = 0:
				player = grid[i][j]
				counter += 1
			elif grid[i][j] != 0 and grid[i][j] == player:
				counter += 1
			elif grid[i][j] == 0 and player != 0:
				counter = 0
				player = 0

	# Checks for diagonal
	for i in range(7-x):
		counter0 = 0
		player0 = 0
		counter1 = 0
		player1 = 0
		for j in range(7-i):
			if grid[i][j] != 0 and player = 0:
				player = grid[i][j]
				counter += 1
			elif grid[i][j] != 0 and grid[i][j] == player:
				counter += 1
			elif grid[i][j] == 0 and player != 0:
				counter = 0
				player = 0






