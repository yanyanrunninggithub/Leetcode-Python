#496. Next Greater Element I
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
	ans = [-1]*len(nums1)
	for i in range(len(nums1)):
		idx = nums2.index(nums1[i])
		for j in range(idx,len(nums2)):
			if nums2[j]>nums1[i]:
				ans[i] = nums2[j]
				break
	return ans
#503. Next Greater Element II
def nextGreaterElements(self, nums: List[int]) -> List[int]:
	ans = [-1]*len(nums)
	for i in range(len(nums)):
		for j in range(1,len(nums)):
			if nums[(i+j)%len(nums)]>nums[i]:
				ans[i] = nums[(i+j)%len(nums)]
				break
	return ans
#556. Next Greater Element III
#approach: scan from right to change the first decrease number to the right side first bigger number and then resort the right part
def nextGreaterElement(self, n: int) -> int:
	if n<=11:
		return -1
	nums = str(n)
	#12443322--->13222344   
	#from back to find the first decrease number
	start = ''
	idx = 0
	ans = ""
	for i in range(len(nums)-1,0,-1):
		if nums[i-1]<nums[i]:
			start = nums[i-1]
			idx = i-1
			break
	ans += nums[0:idx]
	sub = nums[idx+1:len(nums)]
	for i in range(len(sub)-1,-1,-1):
		if sub[i]>start:
			ans += sub[i]#using the first bigger number to put into the idx place
			sub = sub[0:i]+start+sub[i+1:len(sub)]
			break
	#resort the sub array from idx
	sub = sorted(sub)
	for j in range(0,len(sub)):
		ans += sub[j]
	if len(ans) == len(nums):
		return int(ans)
	return -1
