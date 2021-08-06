#448. Find All Numbers Disappeared in an Array
#solution 1:set  better
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        s = set(nums)#if directly check from nums(list), time exceeded, using set save more time
        for n in range(1,len(nums)+1):
            if n not in s:
                res.append(n)
        return res
#solution2: the key idea is to mark the ith element negative if the array contains number i,  iterate the array second time, if jth element is postive, then the number j is missing
 def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            if nums[idx]>0:
                nums[idx] = -nums[idx]
        for i in range(0,len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res