from jabo import JABO
import click

#Let's impliment a simple search tree object. 
#Each node corresponds to a move
#Each node has a list of children (possible subsequent moves) and a 'mapped' bool
#a node gets marked as 'mapped' if the move results in a game over, or if all of its children are 'mapped'


#kind of a funny thing happened here: the tree is also the game manager. 
class SearchNode():
	def __init__(self, parent, move, tree):
		self.tree = tree #the container object
		self.parent = parent #the previous search node object
		self.move = move #the move this node represents. if parent is none, this is the starting gap
		self.children = [] #populated elsewhere
		self.mapped = False

		if self.parent == None:
			self.depth = 0
		else:
			self.depth = self.parent.depth + 1

	def __repr__(self):
		return "Node Depth:{} Move:{} Mapped:{}".format(self.depth, self.move, self.mapped)

	def mark_mapped(self):
		self.mapped = True
		if self.parent is not None:
			self.parent.child_mapped()

	def child_mapped(self):
		#propogate the mapped attribute up the tree, if appropreate
		if False in [child.mapped for child in self.children]:
			pass
		else:
			self.mark_mapped()

	def unmapped_moves(self):
		return [child for child in self.children if not child.mapped]

	def get_branch(self): #basically, get the list of moves which lead to this node
		branch = {}
		branch[self.depth] = self.move
		if self.parent != None:
			return self.parent.get_branch_helper(branch)
		else:
			return branch

	def get_branch_helper(self, branch):
		branch[self.depth] = self.move
		if self.depth == 0:
			return branch
		else:
			return self.parent.get_branch_helper(branch)

	def play_jabo_to_here(self):
		move_branch = self.get_branch()
		jabo = JABO(move_branch[0])
		del move_branch[0]
		for i in range(1, len(move_branch)+1):
			jabo.do_move(move_branch[i])
		return jabo

	def get_children(self):
		board_state = self.play_jabo_to_here()
		next_moves = board_state.get_moves()
		if len(next_moves) > 0:
			for move in next_moves:
				node = SearchNode(self, move, self.tree)
				self.children.append(node)
			for child in self.children:
				child.get_children()
		else:
			self.mark_mapped()
			#print("==================")
			#print(board_state)
			self.tree.games_played += 1
			self.tree.final_state_hist[board_state.pegs_remaining()]+=1 


class SearchTree():
	def __init__(self, starting_gap):
		self.seed = SearchNode(None, starting_gap, self)
		self.games_played = 0
		self.final_state_hist = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}

	def do_search(self):
		self.seed.get_children()
		print("Search completed for starting gap {}".format(self.seed.move))
		print("Games played: {}".format(self.games_played))
		print("Outcome Distribution: {}".format(self.final_state_hist))

if __name__ == "__main__":
	unique_gaps = [0,1,3,4]
	all_gaps = range(15)
	games_played = 0
	hists = []
	for gap in all_gaps:
		tree = SearchTree(gap)
		tree.do_search()
		games_played += tree.games_played
		hists.append(tree.final_state_hist)

	print("Search completed")
	print("total games played: {}".format(games_played))
	print("final outcome hists: {}".format(hists))

