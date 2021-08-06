#720. Longest Word in Dictionary
class Solution(object):
    def longestWord(self, words):#type words: List[str]
        if len(words) == 1:
            return words[0]
        words.sort()//that can guarantee the result order and guarantee that longer word can check shorter word true/false status
        dict = {}
        mx = 0
        ans = ""
        for i in range(0,len(words)):
            length = len(words[i])
            if length == 1 or dict.get(words[i][0:length-1]):
                dict.update({words[i] : True})         
                if length > mx:
                    mx = length
                    ans = words[i]                
        return ans
#594. Longest Harmonious Subsequence
#solution1: dictionary
class Solution(object):
    def findLHS(self, nums):
		dict = {}
        for i in range(len(nums)):
            if (nums[i] in dict.keys()):
                dict[nums[i]] = dict[nums[i]]+1
            else:
                dict.update({nums[i]:1})
        mx = 0        
        for kvp in sorted(dict):#sorted(dict) get a key list
            cnt = dict[kvp]
            if kvp+1 in dict.keys():
                cnt = cnt + dict[kvp+1]
                mx = max(cnt,mx)
        return mx
#solution2: dictionary and in single loop: time O(n) space O(n)
def findLHS(self, nums: List[int]) -> int:
	dict = {}
	cnt = 0
	for i in range(len(nums)):
		if nums[i] not in dict.keys():
			dict.update({nums[i]:1})
		else:
			dict.update({nums[i]:dict[nums[i]]+1})
		if nums[i]+1 in dict.keys():
			cnt = max(cnt,dict[nums[i]]+dict[nums[i]+1])
		if nums[i]-1 in dict.keys():
			cnt = max(cnt,dict[nums[i]]+dict[nums[i]-1])
	return cnt    
#solution3: sort list and tranverse list 
class Solution(object):
    def findLHS(self, nums):
        nums.sort()
        mx=0 
        next_start = 0#when number changed, set a next start idx
        start = 0
        for i in range(1,len(nums)):
            if nums[i]>nums[start]+1:
                start = next_start
            if nums[i]==nums[start]+1:
                mx = max(mx,i-start+1)
            if nums[i] != nums[i-1]:
                next_start = i           
        return mx
#1365. How Many Numbers Are Smaller Than the Current Number
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        map = {}
        ans = sorted(nums)#nums will not changed        
        cnt = 0
        for i in range(len(nums)):
            if ans[i] not in map.keys():
                map.update({ans[i]:cnt})
            cnt += 1
        i=0
        for i in range(len(nums)):
            nums[i] = map[nums[i]]
        return nums
#599. Minimum Index Sum of Two Lists
#Time complexity : O(len1+len2)   Space complexity : O(len1*x) x refers to average string length.
def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
	dict = {}
	for i in range(len(list1)):
		if list1[i] not in dict.keys():
			dict.update({list1[i]:i})
	ans = []
	min_idx = float('inf')
	for i in range(0,len(list2)):
		if list2[i] in dict.keys():
			cnt = dict[list2[i]]+i
			if cnt<min_idx:
				ans.clear()
				ans.append(list2[i])
				min_idx = cnt
			elif cnt==min_idx:
				ans.append(list2[i])
	return ans  
#697. Degree of an Array
#2 hashmap solution: time O(n) space O(n)
def findShortestSubArray(self, nums: List[int]) -> int:
	cnt = {}#store each ele appear cnt
	idx = {}#store each ele left and right idx
	for i in range(len(nums)):
		if nums[i] not in cnt.keys():
			cnt.update({nums[i]:1})
		else:
			cnt[nums[i]] += 1
		if nums[i] not in idx.keys():
			idx.update({nums[i]:[i]})
		else:
			idx[nums[i]].append(i)
	degree = max(cnt.values())
	ans = len(nums)
	for num in cnt.keys():
		if cnt[num] == degree:
			ans = min(ans,idx[num][-1]-idx[num][0]+1)#it may appear multi ele have same degree
	return ans
#1030. Matrix Cells in Distance Order: time  O(N) space O(N)
def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
	map = {} #{distance,index list}
	dist = 0
	for i in range(rows):
		for j in range(cols):
			dist = abs(i-rCenter)+abs(j-cCenter)
			if dist not in map:
				idx = [[i,j]]
				map.update({dist:idx})
			else:
				map[dist].append([i,j])
	ans = []
	for key in sorted(map):#map sorted by keys
		ans += map[key]
	return ans        