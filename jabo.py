import random
#The JABO "Jump all but one" peg game
#
#           (0 )
#        (1 ) (2 )
#      (3 ) (4 ) (5 )
#    (6 ) (7 ) (8 ) (9 )
# (10) (11) (12) (13) (14)


class JABO():
	def __init__(self, start_gap):
		#the keys correspond to the index of each hole
		#the values are lists of tuples.
		#the tuples encode (source, jump)
		#ie, if 5 is empty, 12 can jump 8 to occupy 5, or 14 cand jump 9 to occupy 5. 
		#so the entry for 5 looks like 5:[(12,8), (14,9)]
		self.moves_graph = {
			0:  [(3,1),(5,2)],
			1:  [(6,3),(5,4)],
			2:  [(7,4),(9,5)],
			3:  [(10,6),(0,1),(12,7),(5,4)],
			4:  [(11,7),(13,8)],
			5:  [(12,8),(14,9),(3,4),(0,2)],
			6:  [(1,3),(8,7)],
			7:  [(2,4),(9,8)],
			8:  [(1,4),(6,7)],
			9:  [(7,8),(2,5)],
			10: [(3,6),(12,11)],
			11: [(4,7),(13,12)],
			12: [(10,11),(3,7),(5,8),(14,13)],
			13: [(4,8),(11,12)],
			14: [(12,13),(5,9)]
		}
		#the board state- 1 is a peg, 0 is a hole
		self.board_state = [1]*15 
		self.board_state[start_gap] = 0

	def pegs_remaining(self, ):
		return sum(self.board_state)

	def get_moves(self):
		moves = []
		gaps = [i for i, v in enumerate(self.board_state) if v==0]
		
		for gap in gaps:
			maybe_move = self.moves_graph[gap]
			for move in maybe_move:
				#a move is valid ONLY IF there is a peg alredy in both positions 
				if self.board_state[move[0]] and self.board_state[move[1]]:
					moves.append({"from":move[0], "jump":move[1], "to":gap}) #(source, destination)

		return moves

	def do_move(self, move):
		self.board_state[move["from"]] = 0
		self.board_state[move["jump"]] = 0
		self.board_state[move["to"]] = 1

	def board_string(self):
		return """ 
        ({})
      ({}) ({})
    ({}) ({}) ({})
  ({}) ({}) ({}) ({})
({}) ({}) ({}) ({}) ({})

pegs remaining: {}
		""".format(self.board_state[0], self.board_state[1], self.board_state[2], self.board_state[3], self.board_state[4], self.board_state[5], self.board_state[6],
			self.board_state[7], self.board_state[8], self.board_state[9], self.board_state[10], self.board_state[11], self.board_state[12], self.board_state[13], self.board_state[14], self.pegs_remaining())

	def __repr__(self):
		return self.board_string()

if __name__ == "__main__":
	#Just demonstrating that it works
	for i in range(10):
		jabo = JABO(random.randint(0,14))
		print(jabo.board_string())
		print("Pegs Left: ", jabo.pegs_remaining())
		moves = jabo.get_moves()
		print("Moves: :",moves)
		jabo.do_move(moves[0])
		print(jabo.board_string())
		print("Pegs Left: ", jabo.pegs_remaining())
