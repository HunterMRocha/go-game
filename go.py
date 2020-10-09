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
	for i in range(turns):
		print(f"-------------Round {i+1}-------------")
		# newBoard = ' '.join(map(str, move_x(starting_board))) 
		starting_board = move_x(starting_board)
		print(f"NEW BOARD: {starting_board}")
		x_score = check_kill(starting_board, x_score, o_score)[0]
		if checkWin(x_score, o_score): 
			exit()
		starting_board = move_o(starting_board)
		# newBoard = ' '.join(map(str, move_o(tempBoard)))
		o_score = check_kill(starting_board, x_score, o_score)[1]
		
		print(f"NEW BOARD: {starting_board}")
		print(f"x-score: {x_score}")
		print(f"o-score: {o_score}")

		print("---------------------------------")
		print()

def checkWin(x_score, o_score):
	if x_score + o_score == 10: 
		if x_score > o_score:
			print("X WINS")
			print(f"x-score {x_score}")
			print(f"o-score {o_score}")
			return True
		else: 
			print("O WINS")
			print(f"x-score {x_score}")
			print(f"o-score {o_score}")
			return True
	return False

def check_kill(starting_board, x_score, o_score):
	for i in range(len(starting_board)-2):
		if starting_board[i] == 'x' and starting_board[i+2] == 'x' and starting_board[i+1] == 'o': 
			starting_board[i+1] = '_'
			return x_score + 1, o_score
		elif starting_board[i] == 'o' and starting_board[i+2] == 'o' and starting_board[i+1] == 'x': 
			starting_board[i+1] = '_'
			return x_score, o_score + 1
		
	return x_score, o_score
					
def main():
	x_score = 0
	o_score = 0
	starting_board = list("xxxx__oooo")
	strBoard = ' '.join(map(str,starting_board))
	print("Original Board: ", strBoard)
	print()
	turns = 75
	run_game(turns, starting_board, x_score, o_score)


main()