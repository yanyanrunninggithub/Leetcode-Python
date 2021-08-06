#303. Range Sum Query - Immutable
class NumArray(object):
    def __init__(self, nums):#type nums: List[int]
        self.dp = [0]*len(nums)
        self.dp[0] = nums[0]
        for i in range(1,len(nums)):
            self.dp[i] = self.dp[i-1]+nums[i]
            self.dp[i] = self.dp[i-1]+nums[i]
    def sumRange(self, left, right):
        if left==0:
            return self.dp[right]
        return self.dp[right] - self.dp[left-1]

#997. Find the Town Judge
#approach1: map+list: time O(n) space O(n)
def findJudge(self, n: int, trust: List[List[int]]) -> int:
	if n==1 and len(trust)==0:
		return 1
	impossible = []
	map = {}
	for t in trust:
		impossible.append(t[0])
		if t[1] not in map:
			map.update({t[1]:1})
		else:
			map[t[1]] += 1
		
	for people in map.keys():
		if people not in impossible and map[people] == n-1:
			return people
	return -1
#approach2: list: time O(n) space O(n)  
def findJudge(self, n, trust):
	cnt = [0]*(n+1)
	for pairs in trust:
		cnt[pairs[0]] = cnt[pairs[0]]-1
		cnt[pairs[1]] = cnt[pairs[1]]+1
	for people in range(n+1):
		if cnt[people] == n-1:
			return people
	return -1

#453. Minimum Moves to Equal Array Elements
class Solution(object):
    def minMoves(self, nums):
        #minmove = sum of difference from each ele to the smallest num
        nums.sort()
        min_value = nums[0]
        ans = 0
        for i in range(1,len(nums)):
            ans +=  nums[i]-min_value
        return ans
#solution2:
#sum+moveStep*(length-1)=finalNum*length
#minValue+moveStep = finalNum
#so moveStep = sum-minValue*length
#so moveStep = sum-minValue*length
class Solution(object):
    def minMoves(self, nums):
        return sum(nums) - len(nums) * min(nums)
#1005. Maximize Sum Of Array After K Negations
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        cnt = 0#negative cnt
        cnt0 = 0
        for i in range(len(nums)):
            if nums[i]<0:
                cnt += 1
            elif nums[i]==0:
                cnt0 += 1
            else:
                break
        cur_sum = sum(nums)
        if k<=cnt: # change k nagetive to positive
            for i in range(k):
                if nums[i]<0: 
                    cur_sum += 2*abs(nums[i])
        else: # dif=k-cnt
            for i in range(cnt):
                if nums[i]<0: 
                    cur_sum += 2*abs(nums[i])
            dif = k-cnt
            """if cnt0>0 or (dif%2==0):
                return cur_sum"""
            if cnt0==0 and (dif%2 == 1):
                # get minum abs to flip, minum abs must from nums[cnt-1] or nums[cnt]
                if cnt== 0:#no negative num
                    cur_sum = cur_sum-2*nums[cnt]
                else:
                    cur_sum = cur_sum-2*min(abs(nums[cnt-1]),abs(nums[cnt]))
        return cur_sum
#605. Can Place Flowers: time O(n) space O(1)
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
	if n<1:
		return True
	cnt = 0
	for i in range(len(flowerbed)):
		if flowerbed[i] == 0:
			if (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
				cnt += 1
				flowerbed[i] = 1
				if cnt>=n:
					return True
	return False
#821. Shortest Distance to a Character:For each index S[i], let's try to find the distance to the next character C going left, and going right. The answer is the minimum of these two values. Time O(n) space O(n)
 def shortestToChar(self, s: str, c: str) -> List[int]:
	ans = [float('inf')]*len(s)
	idx = float('-inf')
	for i in range(0,len(s)):#from left to right
		if s[i] == c:
			idx = i
		ans[i] = min(i-idx,ans[i])
	idx = float('inf')
	for i in range(len(s)-1,-1,-1):#from right to left
		if s[i] == c:
			idx = i
		ans[i] = min(idx-i,ans[i])
	return ans
#830. Positions of Large Groups:  time O(n) space O(n)
def largeGroupPositions(self, s: str) -> List[List[int]]:
	res = []
	if len(s)<3:
		return res
	i=0
	while i<len(s):
		ch = s[i]
		start = i
		while i+1<len(s) and s[i+1] == ch:
			i = i+1
		if i>=start+2 :#end=i
			r = [start,i]
			res.append(r)
		i = i+1		
	return res
#888. Fair Candy Swap: time o(m+n) space o(1)
def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
	Sa, Sb = sum(aliceSizes), sum(bobSizes)
	for x in aliceSizes:
		y =  (x + (Sb - Sa) // 2)
		if y in bobSizes:
			return [x,y]
#941. Valid Mountain Array: time O(n) space O(1)
def validMountainArray(self, A):
        N = len(A)
        i = 0
        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1
        # peak can't be first or last
        if i == 0 or i == N-1:
            return False
        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1
        return i == N-1

        