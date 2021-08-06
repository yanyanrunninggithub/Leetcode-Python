#9. Palindrome Number
#solution1: using list
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        list = []
        while x !=0 :
            list.append(x%10)
            x = x//10##//means floor divide
        i=0
        j=len(list)-1
        while i<=j:
            if list[i]!=list[j]:
                return False
            else:
                i = i+1
                j = j-1
                
        return True
#solution2: reverse the int
class Solution(object):
    def isPalindrome(self, x):
        def reverse(x):
            y = 0
            while x!=0:
                y = y*10 +x%10
                x = x//10
            return y
        
        if x<0:
            return False
        y = reverse(x)
        return True if x==y else False #python return condition
#409. Longest Palindrome
class Solution(object):
    def longestPalindrome(self, s):
        cnt = [0]*52
        length = 0
        flag = False
        for i in range(len(s)):
            if s[i].isupper():
                cnt[ord(s[i])-ord('A')] += 1
            else:
                cnt[ord(s[i])-ord('a')+26] += 1
        for i in range(52):
            if cnt[i]%2 == 0:
                length += cnt[i]
            else:
                flag = True
                length += cnt[i]-1
        return (length+1) if flag else length
#5. Longest Palindromic Substring
#Approach1: brute force: Time o(n^3),space O(1)
def getLongestPanlindrome(s:str)->str:
    max = 1
    ans = s[0]
    for start in range(len(s)):
        for end in range(start+1,len(s)):
            flag = True
            
            for i in (0,(end-start)//2+1):                
                if s[start+i] != s[end-i]:
                    flag = False
                    break
            """print(start)
            print(end)"""
            if flag and (end-start+1)>max:
                ans = s[start:end+1]
                max = end-start+1
    return ans  
#Approach2: dynamic programming: Time o(n^2),space O(n^2)
def getLongestPanlindrome(s:str)->str:
    max = 1
    ans = s[0]
    n = len(s)
    dp = [[False for x in range(n)] for y in range(n)]
    #substr len = 1
    for i in range(len(s)):
        dp[i][i] = True
    #substr len = 2
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            max = 2
            ans = s[i:i+2]
    for sublen in range(3,len(s)+1):#j is sublen
        i=0
        while i <(n-sublen+1):
            end = i+sublen-1
            if (s[i] == s[end]) and dp[i+1][end-1]:
                dp[i][end] = True
                if sublen>max:
                    ans = s[i:end+1]
                    max = sublen
            i += 1
    print(dp)
    return ans
#Approach3: middle pointer: expand from middle to both directions: Time o(n^2),space O(1)
def expand(s:str,start:int,end:int)->str:
    while start>=0 and end<len(s) and s[start] == s[end]:
        start -= 1
        end += 1
    return s[start+1:end]
def getLongestPanlindrome(s:str)->str:
    max = 1
    ans = s[0]
    n = len(s)
    for i in range(0,n):
        odd = expand(s,i,i)#length is odd, so middle pointer is same index
        if len(odd) > max:
            max = len(odd)
            ans = odd
        even = expand(s,i,i+1)#length is even, so middle pointer is i and i+1
        if len(even) > max:
            max = len(even)
            ans = even
    return ans
#125. Valid Palindrome time O(n) space O(n)
def isPalindrome(self, s: str) -> bool:
	p = 0
	q = len(s)-1
	while p<q:
		if s[q].isalpha() == False and s[q].isdigit() == False:
			q -= 1
			continue
		if s[p].isalpha() == False and s[p].isdigit() == False:
			p += 1
			continue
		if s[p].lower() != s[q].lower():
			return False
		p += 1
		q -= 1
	return True	
#680. Valid Palindrome II
#Greedy, delete the first unmatched char        time O(n)
 def validPalindrome(self, s: str) -> bool:
	def isvalid(s:str, left:int, right:int) -> bool:
		while left<right:
			if s[left] != s[right]:
				return False
			left += 1
			right -= 1
		return True
	p = 0
	q = len(s)-1
	while p<q:
		if s[p] != s[q]:
			return isvalid(s,p+1,q) or isvalid(s,p,q-1)
		p += 1
		q -= 1
	return True
	