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
#844. Backspace String Compare
#approach1: build each str: time O(M+N) space O(M+N)
 def backspaceCompare(self, s: str, t: str) -> bool:
	def build(s):
		ans = []
		for c in s:
			if c=='#':
				if len(ans)>0:
					ans.pop()
			else:
				ans.append(c)
		return ans
	return build(s) == build(t)
#approach2: compare from end and 2 pointer: time O(M+N) space O(1)
def backspaceCompare(self, s: str, t: str) -> bool:
	cnt1 = 0
	cnt2 = 0
	p = len(s)-1
	q = len(t)-1
	while p>=0 or q>=0:
		while (p >= 0): # Find position of next possible char in build(S)
			if (s[p] == '#'):
				cnt1 += 1
				p -= 1
			elif (cnt1 > 0):
				cnt1 -= 1
				p -= 1
			else:
				break
		while (q >= 0): # Find position of next possible char in build(T)
			if (t[q] == '#'):
				cnt2 += 1
				q -= 1
			elif (cnt2 > 0):
				cnt2 -= 1
				q -= 1
			else:
				break
		if (p>=0 and q<0) or (q>=0 and p<0):
			return False
		if s[p]!= t[q]:
			return False
		p -= 1
		q -= 1
	return True
#905. Sort Array By Parity: time o(n) space O(1)
def sortArrayByParity(self, nums: List[int]) -> List[int]:
	i, j = 0, len(nums) - 1
	while i < j:
		if nums[i] % 2 > nums[j] % 2:
			nums[i], nums[j] = nums[j], nums[i]
		if nums[i] % 2 == 0: i += 1
		if nums[j] % 2 == 1: j -= 1
	return nums
#942. DI String Match: time O(n) space O(n)
def diStringMatch(self, S):
	lo, hi = 0, len(S)
	ans = []
	for x in S:
		if x == 'I':#should increase
			ans.append(lo)
			lo += 1
		else:#should decrease
			ans.append(hi)
			hi -= 1
	return ans + [lo]
#977. Squares of a Sorted Array: time O(n) space O(n)
def sortedSquares(self, nums: List[int]) -> List[int]:
	ans = [0]*len(nums)
	idx = len(nums)-1
	p,q = 0, len(nums)-1
	while idx>=0:
		if abs(nums[q])>=abs(nums[p]):
			ans[idx] = nums[q]*nums[q]
			q -= 1
		else:
			ans[idx] = nums[p]*nums[p]
			p += 1
		idx -= 1
	return ans	