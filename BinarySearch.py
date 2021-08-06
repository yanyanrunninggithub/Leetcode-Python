#The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n). 
#704. Binary Search
def search(self, nums: List[int], target: int) -> int:
	left, right = 0, len(nums) - 1
	while left <= right:
		pivot = left + (right - left) // 2
		if nums[pivot] == target:
			return pivot
		if target < nums[pivot]:
			right = pivot - 1
		else:
			left = pivot + 1
	return -1
#35. Search Insert Position
def searchInsert(self, nums, target):
	p = 0
	q = len(nums)-1
	while p<=q:
		mid = p+(q-p)//2
		if nums[mid] == target:
			return mid
		elif nums[mid]<target:
			p = mid+1
		else:
			q = mid-1
	return p
@278. First Bad Version
class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start<end:
            mid = start + (end-start)//2
            if isBadVersion(mid-1)==False and isBadVersion(mid):
                return mid
            if isBadVersion(mid) == False:
                start = mid+1
            else:
                end = mid-1
        return start
#441. Arranging Coins
def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left<=right:
            cur = left + (right-left)//2
            sum = cur*(cur+1)//2
            if sum == n:
                return cur
            if sum<n:
                left = cur+1
            else:
                right = cur-1
        return right
#852. Peak Index in a Mountain Array: time O(logN) space O(1)
 def peakIndexInMountainArray(self, A):
	lo = 0
	hi = len(arr) - 1
	while lo < hi:
		mi = lo+ ( hi-lo) // 2
		if arr[mi] < arr[mi + 1]:
			lo = mi + 1
		else:
			hi = mi
	return lo