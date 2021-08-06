 #566. Reshape the Matrix
 def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
	m = len(mat)
	n = len(mat[0])
	if m*n != r*c:
		return mat
	ans = [[0 for x in range(c)] for y in range(r)]
	for i in range(0,r*c):
		ans[i//c][i%c] = mat[i//n][i%n]
	return ans
#463. Island Perimeter
#Approach1:
def islandPerimeter(self, grid: List[List[int]]) -> int:
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    sum += 4
                    if i!=0 and grid[i-1][j]==1:
                        sum -= 1
                    if i!=len(grid)-1 and grid[i+1][j]==1:
                        sum -= 1
                    if j!=0 and grid[i][j-1]==1:
                        sum -= 1
                    if j!=len(grid[0])-1 and grid[i][j+1]==1:
                        sum -= 1
        return sum
#Approach 2: only search for the up and left  better
def islandPerimeter(self, grid: List[List[int]]) -> int:
	land = 0
	edge = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				land += 1
				if i!=0 and grid[i-1][j]==1:
					edge += 1
				if j!=0 and grid[i][j-1]==1:
					edge += 1
	return (land*4-edge*2)
#867. Transpose MatrixL: time O(R*C) space O(R*C)
def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
	R, C = len(matrix), len(matrix[0])#input 2d-list size is C*R
	ans = [[0 for x in range(R)] for y in range(C)]#return 2d-list size is R*C, return matrix size is also transposed so we should build a new return 2d-list
	for r in range(R):
		for c in range(C):
			ans[c][r] = matrix[r][c]
	return ans
#874. Walking Robot Simulation: time o(n) space O(n)
def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
	dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]#from west,north,east to south
	x,y = 0, 0#each step can go place
	cur_x,cur_y = 0, 0#without considering obstacles each step index
	d = 1#north is initial val
	ans = 0
	for c in commands:
		if c == -1:
			d = (d+1)%4 #get direction
		elif c == -2:
			d = (d+4-1)%4
		else:
			while(c>0):
				cur_x =x+ dir[d][0]
				cur_y =y+ dir[d][1]
				idx = [cur_x,cur_y]
				if idx in obstacles:
					break
				x = cur_x
				y = cur_y
				c -= 1
			ans = max(ans,x*x+y*y)
	return ans