import random

x_pos = [0,1,2,3]
o_pos = [6,7,8,9]
open_spots = [4,5]

def move_x(starting_board):
	#randomly pick an x piece and an empty spot
	p1 = random.choice(x_pos)
	p1_placement = random.choice(open_spots)
	print(f"X-CHOICE: {p1} -> {p1_placement}")

	#assign new location
	starting_board[p1_placement] = "x"
	starting_board[p1] = "_"

	#update indexes for x_pos, o_pos, and open_spots
	x_pos.remove(p1)
	x_pos.append(p1_placement)

	open_spots.remove(p1_placement)
	open_spots.append(p1)
	return starting_board

def move_o(starting_board):
	p2 = random.choice(o_pos)
	p2_placement = random.choice(open_spots)
	print(f"O-CHOICE: {p2} -> {p2_placement}")

	#assign new location
	starting_board[p2_placement] = "o"
	starting_board[p2] = "_"

	#update indexes for x_pos, o_pos, and open_spots
	o_pos.remove(p2)
	o_pos.append(p2_placement)

	open_spots.remove(p2_placement)
	open_spots.append(p2)
	return starting_board

def run_game(turns, starting_board, x_score, o_score):
	alive = True
	idx_to_kill = []
	while(alive):
		for i in range(turns):
			print(f"-------------Round {i+1}-------------")
			starting_board = move_x(starting_board)
			tempBoard = ' '.join(map(str,starting_board))
			idx_to_kill = check_kill(starting_board)
			print('o-indexes to kill', idx_to_kill)

			if len(idx_to_kill) > 0: 
				kill(starting_board, x_score, o_score, idx_to_kill)
				x_score = update_score(starting_board, x_score, o_score, idx_to_kill, alive)[0]
				o_score = update_score(starting_board, x_score, o_score, idx_to_kill, alive)[1]
				if checkWin(x_score, o_score, alive): 
					alive = False

			print(f"NEW BOARD: {tempBoard}")

			starting_board = move_o(starting_board)
			tempBoard = ' '.join(map(str,starting_board))

			idx_to_kill = check_kill(starting_board)
			print('x-indexes to kill', idx_to_kill)


			if len(idx_to_kill) > 0: 
				kill(starting_board, x_score, o_score, idx_to_kill)
				x_score = update_score(starting_board, x_score, o_score, idx_to_kill, alive)[0]
				o_score = update_score(starting_board, x_score, o_score, idx_to_kill, alive)[1]
				if checkWin(x_score, o_score, alive): 
					alive = False
			
			print(f"NEW BOARD: {tempBoard}")

			print(f"x-score: {x_score}")
			print(f"o-score: {o_score}")

			print("---------------------------------")
			print()

def checkWin(x_score, o_score, alive):
	if x_score + o_score == 10: 
		alive = False
		if x_score > o_score:
			print("X WINS")
			print(f"x-score {x_score}")
			print(f"o-score {o_score}")
		else: 
			print("O WINS")
			print(f"x-score {x_score}")
			print(f"o-score {o_score}")
	return alive

def check_kill(starting_board):
	indexes_to_kill = []
	#x_xoox_xoo
	for i in range(len(starting_board)-1):
		if starting_board[i] == 'x' and starting_board[i+1] == 'o':
			for j in range(i+1, len(starting_board)):
				if starting_board[j] == 'x':
					print('indexes', indexes_to_kill)
					return indexes_to_kill
				elif starting_board[j] == '_':
					indexes_to_kill.clear()
					break
				else: 
					indexes_to_kill.append(j)
		elif starting_board[i] == 'o' and starting_board[i+1] == 'x':
			for j in range(i+1, len(starting_board)):
				if starting_board[j] == 'o':
					return indexes_to_kill
				elif starting_board[j] == '_':
					indexes_to_kill.clear()
					break
				else: 
					indexes_to_kill.append(j)
	return indexes_to_kill

def update_score(starting_board, xscore, oscore, idx_to_kill, alive):
	if not idx_to_kill: 
		return xscore, oscore
	new_points = len(idx_to_kill)
	kill = starting_board[idx_to_kill[0]]
	if(kill == 'o'):
		xscore += new_points
		if checkWin(xscore, oscore, alive): 
				alive = False
	elif kill == 'x': 
		oscore += new_points
	return xscore, oscore

def kill(starting_board, xscore, oscore, idx_to_kill):
	for i in idx_to_kill: 
		open_spots.append(i)
		starting_board[i] = '_'
					
def main():
	x_score = 0
	o_score = 0
	starting_board = list("xxxx__oooo")
	strBoard = ' '.join(map(str,starting_board))
	print("Original Board: ", strBoard)
	print()
	turns = 8000
	run_game(turns, starting_board, x_score, o_score)


main()