#746. Min Cost Climbing Stairs
#time O(n) space O(n)
def minCostClimbingStairs(self, cost: List[int]) -> int:
	dp = [0]*(len(cost)+1)
	for i in range(2,len(cost)+1):
		dp[i] = min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
	return dp[len(cost)]
#70. Climbing Stairs time O(n) space O(n)
def climbStairs(self, n: int) -> int:
	if n==1:
		return 1
	
	dp = [1]*(n+1)
	for i in range(2,n+1):
		dp[i] = dp[i-1]+dp[i-2]
	return dp[n]