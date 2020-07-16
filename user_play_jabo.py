#play jabo
from jabo import JABO


#play loop:
# 1. user designates starting gap
# 2. get list of possible moves
# 3. present user list of moves (numberd)
# 4. user picks move
# 5. make move
# 6. repeat from 2

def start():
	startgap = int(raw_input("Starting Gap: "))
	jabo = JABO(startgap)
	print(jabo)
	make_move(jabo)

def make_move(jabo):
	moves = jabo.get_moves()
	if len(moves) > 0:
		print("possible moves:")
		for line in [(index, move) for index, move in enumerate(moves)]:
			print("{} : {}".format(line[0], line[1]))

		move_input = int(raw_input("Make move #: "))
		jabo.do_move(moves[move_input])
		print(jabo)
		make_move(jabo)
	else:
		print("Game Over!")
		print("{} pegs remaining!".format(jabo.pegs_remaining()))
		next_ = raw_input("Press Y to start again, Q to quit")
		if next_ == "Y":
			start()
		


if __name__ == "__main__":
	start()
