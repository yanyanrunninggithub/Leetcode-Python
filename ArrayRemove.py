#26. Remove Duplicates from Sorted Array: 2pointers approach
class Solution(object):
    def removeDuplicates(self, nums):
        p = 0
        for q in range(1, len(nums)):
            if nums[q]!=nums[p]:
                p += 1
                nums[p] = nums[q]
        return p+1
#27. Remove Element
#approach1: 2 pointers
class Solution(object):
    def removeElement(self, nums, val):
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx = idx+1
        return idx
#approach2: the number of assignment operations is equal to the number of elements to remove, so less assignment operations when elements to remove are rare
class Solution(object):
    def removeElement(self, nums, val):
        p = 0
        q = len(nums)      
        while p<q:
            if nums[p] == val:
                nums[p] = nums[q-1]
                q -= 1
            else:
                p += 1
        return q
#283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
				#swap idx and i, The total operations (array writes) that code does is Number of non-0 elements.
                t = nums[idx]
                nums[idx] = nums[i]
                nums[i] = t
                idx += 1
#1089. Duplicate Zeros
class Solution(object):
    def duplicateZeros(self, arr):
        i=0
        length = len(arr)
        while i<length:
            if arr[i] !=0 :
                i += 1
            else:
                arr.insert(i,0)
                del arr[-1]
                i += 2