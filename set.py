#500. Keyboard Row  O(m*n)
def findWords(self, words: List[str]) -> List[str]:
        set1 = set("qwertyuiop") #build set is o(n)
        set2 = set("asdfghjkl")
        set3 = set("zxcvbnm")
        ans = []
        for word in words:#o(m)
            if set(word.lower()) <= set1: #judge set in subset of another one
                ans.append(word) 
            if set(word.lower()) <= set2:
                ans.append(word) 
            if set(word.lower()) <= set3:
                ans.append(word) 
        return ans
#575. Distribute Candies   
#Approach 1: set   Time O(n)(creating set), space O(n)(set space)
def distributeCandies(self, candyType: List[int]) -> int:
    return min(len(set(candyType)),len(candyType)//2)
#Approach 2: sort and count  Time O(NLogN) for sort and space O(N) Python and Java now use Timsort, which requires O(N)O(N) space.
def distributeCandies(self, candyType: List[int]) -> int:
	if len(candyType)<2:
		return 0
	candyType.sort()
	pre = candyType[0]
	cnt = 1
	for i in range(1,len(candyType)):
		if candyType[i]!= pre:
			cnt += 1
			pre = candyType[i]
	return cnt if cnt<=len(candyType)//2 else len(candyType)//2
#1461. Check If a String Contains All Binary Codes of Size K
#Time complexity: O(NK). We need to iterate the string, and use O(K) to calculate the hash of each substring.
#Space complexity:O(NK). There are at most N strings with length K in the set.
def hasAllCodes(self, s: str, k: int) -> bool:
	got = set()
	cnt = 1<<k #total number of different conbination for length k
	for i in range(0,len(s)-k+1): #traverse str to find all unique k length substr
		sub = s[i:i+k] #time O(k)
		if sub not in got: #set in O(1),list in is O(n)
			got.add(sub)
			cnt -= 1
			if cnt == 0:
				return True
	return False