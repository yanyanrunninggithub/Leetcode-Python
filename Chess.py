#999. Available Captures for Rook
#DFS:time O(M*N) space O(1)
def numRookCaptures(self, board: List[List[str]]) -> int:
	x0,y0 = 0,0
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 'R':
				x0 = i
				y0 = j
				break
	dir = [[-1,0],[0,1],[1,0],[0,-1]]
	ans = 0
	for d in dir:
		x = d[0]+x0
		y = d[1]+y0
		while x>=0 and x<len(board) and y>=0 and y<len(board[0]):                
			if board[x][y] == 'p':
				ans += 1
			if board[x][y] != '.':
				break
			x += d[0]
			y += d[1]
	return ans