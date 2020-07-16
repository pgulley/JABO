from jabo import JABO
import random
import click
#A cacheless random strategy to find a jabo solution

starting_gaps = [0,1,3,4] #since the board has lots of symmetry, we don't have to test every possible starting gap.

#play loop:
# 1. randomly pick starting gap
# 2. get list of possible moves
# 3. randomly pick move
# 4. make move
# 5. repeat from 2


def start_random_game(v):
	jabo_board = JABO(random.choice(starting_gaps))
	if v=="a":
		print(jabo_board)
	make_move(jabo_board, v)


def make_move(jabo_board, v):
	possible_moves = jabo_board.get_moves()
	if len(possible_moves) > 0:
		move = random.choice(possible_moves)
		jabo_board.do_move(move)
		if v=="a":
			print(jabo_board)
		make_move(jabo_board, v)
	else:
		print("game over with {} pegs remaining!".format(jabo_board.pegs_remaining()))
		return

@click.command()
@click.option("--its", prompt="Iterations: ", type=int, help="Number of iterations of random strategy to run")
@click.option("--v", default="o", type=click.Choice(["a", "o"]), help="log verbosity setting. a: print game state and outcome, o: print game outcome only (default)")
def random_strat(its, v):
	for i in range(its):
		start_random_game(v)

if __name__ == "__main__":
	random_strat()


