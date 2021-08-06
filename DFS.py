#401. Binary Watch
from itertools import combinations
class Solution:   
    def dfs(self,n:int, h:int, res: List):
        if h>3 or h>n:
            return
        for hour in combinations([1,2,4,8],h):
            h_time = sum(hour)
            if h_time>11:
                continue
            s = str(h_time)+":"
            for mins in combinations([1,2,4,8,16,32],n-h):
                m_time = sum(mins)
                if m_time>59:
                    continue
                elif m_time<10:
                    res.append(s+ "0"+str(m_time))
                else:
                    res.append(s+str(m_time))
        self.dfs(n,h+1,res)
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn>8:
            return []
        res = []
        self.dfs(turnedOn,0, res)
        return res
#leetcode200. Number of Islands   Time O(m*n) space o(m*n)
class Solution:
    def dfs(self,grid:List[List[str]],visited:List[List[int]],x:int,y:int):        
        if x<0 or x>=len(grid):
            return
        if y<0 or y>=len(grid[0]):
            return
        if grid[x][y] == "0" or visited[x][y] == 1:
            return
        visited[x][y] = 1
        self.dfs(grid,visited,x-1,y)
        self.dfs(grid,visited,x+1,y)   
        self.dfs(grid,visited,x,y-1)
        self.dfs(grid,visited,x,y+1)
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    cnt += 1
                    self.dfs(grid,visited,i,j)
        return cnt
#690. Employee Importance
#Time Complexity: O(N), where N is the number of employees. We might query each employee in dfs. Space O(n)
def getImportance(self, employees: List['Employee'], id: int) -> int:
	map = {}
	for e in employees:
		map.update({e.id:e})# map = {id: employee class}
	
	def dfs(id: int) -> int:#sub function to depth first search
		subordinate = map[id].subordinates
		key =  map[id].importance
		for sub in subordinate:
			key += dfs(sub)
		return key
	return dfs(id)
#733. Flood Fill time O(m*n) space O(m*n)//the size of the implicit call stack when calling dfs
def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
	oldColor = image[sr][sc]
	if oldColor == newColor:
		return image
	m = len(image)
	n = len(image[0])
	
	def dfs(x,y):
		if image[x][y] == oldColor:
			image[x][y] = newColor
			if x>0:
				dfs(x-1,y)
			if x<m-1:
				dfs(x+1,y)
			if y>0:
				dfs(x,y-1)
			if y<n-1:
				dfs(x,y+1)
	dfs(sr,sc)
	return image