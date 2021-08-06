#53. Maximum Subarray time O(N) space O(1)
def maxSubArray(self, nums: List[int]) -> int:
	cur = nums[0]
	mx = cur
	for i in range(1,len(nums)):
		cur += nums[i]
		cur = max(cur,nums[i])
		mx = max(mx,cur)
	return mx
#643. Maximum Average Subarray I time O(N) space O(1)
def findMaxAverage(self, nums: List[int], k: int) -> float:
	sum = 0
	for i in range(k):
		sum += nums[i]
	ans = sum/k
	for i in range(k,len(nums)):
		sum = sum-nums[i-k]+nums[i]
		ans = max(ans,sum/k)
	return ans
#674. Longest Continuous Increasing Subsequence
#time O(n) space O(1)
def findLengthOfLCIS(self, nums: List[int]) -> int:
	cnt = 0
	start = 0
	i = 0
	for i in range(1,len(nums)):
		if nums[i]<=nums[i-1]:
			cnt = max(cnt,i-start)
			start = i
	#the last sub not update
	cnt = max(cnt,i-start+1)#jump out i == len(nums)-1
	return cnt
#1013. Partition Array Into Three Parts With Equal Sum: time O(n) space O(1)
def canThreePartsEqualSum(self, arr: List[int]) -> bool:
	sum0 = sum(arr)
	if sum0%3 != 0:
		return False
	target = sum0//3
	cnt = 0
	cur_sum = 0
	for i in range(len(arr)):
		cur_sum += arr[i]
		if cur_sum==target:
			cur_sum = 0
			cnt += 1
	return (cnt>=3)