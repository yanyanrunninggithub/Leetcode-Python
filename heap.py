#minheap--->k largest, heapq is min heap
#maxheap--->k smallest
#703. Kth Largest Element in a Stream 
#approach1: using heapq
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)#heapq is a minheap
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):#o(logK)
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        else:
            heapq.heappush(self.heap,val)
            heapq.heappop(self.heap)
        return self.heap[0]
#approach 2: using list  time O(nlogn)
def __init__(self, k: int, nums: List[int]):
	self.k = k
	self.nums = nums
	self.min_heap = nums
	self.min_heap.sort()
	if len(self.min_heap)>k:
		self.min_heap.pop(0)
def add(self, val: int) -> int:
	self.min_heap.append(val)
	self.min_heap.sort()
	if len(self.min_heap)>self.k:
		self.min_heap.pop(0)
	return self.min_heap[0]
#20210622 amazon phone interview: get the kth star's name which its distance is kth smallest in the list
#time complexity: O(k + (n-k)*Logk)
def getKSmall(list):
	max_heap = []
	for i in range(k):
		max_heap.append(list[i])
	for j in range(k,len(list)):
		max_heap.sort().reverse()#create a max heap, heap[0] is the biggest
		if list[i]<max_heap[0]:
			max_heap.pop(0)#The time complexity of heap push/pop is o(logk)and we do it N - k times
			max_heap.append(list[i])
	return max_heap[0]
#347. Top K Frequent Elements
#approach 1: map O(N)+o(NlogN) 
class Solution(object): 
    def topKFrequent(self, nums, k):
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map.keys():
                map.update({nums[i]:nums.count(nums[i])})
        
        ans = []
        for num in dict(sorted(map.items(),key=lambda x:x[1],reverse=True)):#num is a key
            if k<=0:
                break
            ans.append(num)
            k -=1
        return ans
#approach 2:minheap   o(N)+O(Nlogk) 
class Solution(object):
    def topKFrequent(self, nums, k):
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map.keys():
                map.update({nums[i]:nums.count(nums[i])})
        return heapq.nlargest(k, map.keys(), key=map.get)
#414. Third Maximum Number (distinct)		
 def thirdMax(self, nums: List[int]) -> int:
        #min heap
        res = []
        if len(nums)<3:
            return max(nums)
        for i in range(len(nums)):
            if nums[i] not in res:#check distinct or not
                if len(res)<3:
                    res.append(nums[i])
                elif len(res)==3 and nums[i]>res[0]:#using elif, in case of previous line append
                    res.pop(0)
                    res.append(nums[i])
                res.sort()
        if len(res)<3:
            return res[-1]
        return res[0]
#1046. Last Stone Weight
#Aproach 2:maxheap using list: time O(nlogn) space o(1)
 def lastStoneWeight(self, stones: List[int]) -> int:
	#max-heap
	stones.sort()
	while len(stones)>=2:
		x1 = stones[-1]
		x2 = stones[-2]
		stones.pop()
		stones.pop()
		if x1!=x2:
			stones.append(x1-x2)
		stones.sort()
	if len(stones) == 1:
            return stones[0]
	else:
		return 0 
#Aproach 2:minheap using heapq
def lastStoneWeight(self, stones: List[int]) -> int:
	heap=[]
	for stone in stones:
		heapq.heappush(heap,-stone)#min-heap, but using its negative val, so the biggest digitive num is smallest negetive val
	while len(heap)>=2:
		x1 = heapq.heappop(heap)
		x2 = heapq.heappop(heap)
		if x1 != x2:
			heapq.heappush(heap,(x1-x2))
	return -heap[-1] if heap else 0        