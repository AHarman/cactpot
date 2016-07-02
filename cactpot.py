
class CactpotBoard:
	board = [[None, None, None],
	         [None, None, None],
	         [None, None, None]]
	
	"""
	Possible "lines" are numbered like this, going from the number/index through the Xs
	i.e 7 goes diagonally like ths /, 3 goes diagonally like \, 2 goes like - and 5 goes like |

	3 4 5 6 7
	2 X X X
	1 X X X
	0 X X X
	"""
	
	numbersLeft = range(1, 10)

	rewards = {  6: 10000,
	             7:    36,
	             8:   720,
	             9:   360,
	            10:    80,
	            11:   252,
	            12:   108,
	            13:    72,
	            14:    54,
	            15:   180,
	            16:    72,
	            17:   180,
	            18:   119,
	            19:    36,
	            20:   306,
	            21:  1080,
	            22:   144,
	            23:  1800,
	            24:  3600}

	def __init__(self, board=None):
		if board != None:
			self.board = board
			numbers = [n for n in board[0]+board[1]+board[2] if n]
			self.numbersLeft = [n for n in range(1, 10) if n not in numbers]

	def __str__(self):
		numbers = [str(n) if n else " " for n in self.board[0]+self.board[1]+self.board[2]]
		string =  "3   4   5   6   7\n"
		string += "  +---+---+---+\n"
		string += "2 | " + numbers[0] + " | " + numbers[1] + " | " + numbers[2] + " |\n"
		string += "  +---+---+---+\n"
		string += "1 | " + numbers[3] + " | " + numbers[4] + " | " + numbers[5] + " |\n"
		string += "  +---+---+---+\n"
		string += "0 | " + numbers[6] + " | " + numbers[7] + " | " + numbers[8] + " |\n"
		string += "  +---+---+---+"
		return string

	def updateBoard(self, row, col, value):
		self.board[row][col] = value
		self.numbersLeft = [x for x in self.numbersLeft if x != value]

	def getLine(self, lineNum):
		if lineNum == 0:
			return self.board[2]
		elif lineNum == 1:
			return self.board[1]
		elif lineNum == 2:
			return self.board[0]
		elif lineNum == 3:
			return [self.board[0][0], self.board[1][1], self.board[2][2]]
		elif lineNum == 4:
			return [self.board[0][0], self.board[1][0], self.board[2][0]]
		elif lineNum == 5:
			return [self.board[0][1], self.board[1][1], self.board[2][1]]
		elif lineNum == 6:
			return [self.board[0][2], self.board[1][2], self.board[2][2]]
		elif lineNum == 7:
			return [self.board[0][2], self.board[1][1], self.board[2][0]]

	def lineExpectedValue(self, lineNum):
		line = [x for x in self.getLine(lineNum) if x != None]

		if len(line) == 3:      # If you screwed up and got 3 in a row, you can't get a reward for it
			return 0
		elif len(line) == 2:
			return sum([self.rewards[num + sum(line)] for num in self.numbersLeft]) / len(self.numbersLeft)
		elif len(line) == 1:
			total = 0
			num = 0
			for i in range(len(self.numbersLeft)):
				for j in range(i + 1, len(self.numbersLeft)):
					total += self.rewards[line[0] + self.numbersLeft[i] + self.numbersLeft[j]]
					num += 1
			return total / num

		elif len(line) == 0:
			total = 0
			num = 0
			for i in range(len(self.numbersLeft)):
				for j in range(i + 1, len(self.numbersLeft)):
					for k in range(j + 1, len(self.numbersLeft)):
						total += self.rewards[self.numbersLeft[i] + self.numbersLeft[j] + self.numbersLeft[k]]
						num += 1
			return total / num

	def boardExpectedValue(self):
		return max([self.lineExpectedValue(x) for x in range(8)])       # We're always going to pick the best one

cpb = CactpotBoard()
cpb.updateBoard(0, 0, 1)
cpb.updateBoard(1, 1, 2)
print cpb
print cpb.boardExpectedValue()