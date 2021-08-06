def split(s:str) -> str:
    ans = []
    word = ""
    for letter in s:
        if letter == ' ':
            ans.append(word)
            word = ""
        else:
            word += letter
    ans.append(word)
    return ans
#541. Reverse String II
class Solution(object):
    def reverseStr(self, s, k):#s is string, k is int
        cnt = len(s)//k
        ans = ""
        for i in range(cnt+1):
            sub = ""
            if (i*k+k)>len:
                sub = s[i*k:len(s)]
            else:
                sub = s[i*k:i*k+k]
            if i%2==0:#even need to reserve
                ans = ans + sub[::-1] 
            else:
                ans = ans + sub
        return ans
		
#1576. Replace All ?'s to Avoid Consecutive Repeating Characters
class Solution(object):
    def get_good_char(self,s,idx,ans):
        if len(s) == 1:
            return 'a'
        alphabet  = string.ascii_lowercase
        for ch in alphabet:
            #ch = 'a'+i
            if (idx==0) and s[idx+1]!=ch:
                return ch
            if (idx==len(s)-1) and ans[idx-1]!=ch:#if double ? appear, the first one has changed so we should check ans string to get its previous char and get its next from s string
                return ch
            if (idx>0) and (idx<(len(s)-1)) and s[idx+1]!=ch and ans[idx-1]!=ch:
                return ch
    def modifyString(self, s):
        ans = ""#string is immutable so we should create a new result string
        for i in range(len(s)):
            if s[i] == '?':
                ans = ans + self.get_good_char(s,i,ans)
            else:
                ans = ans + s[i]
        return ans
#1071. Greatest Common Divisor of Strings
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if(len(str1)<len(str2)):
            tmp = str1
            str1 = str2
            str2 = tmp
        len1 = len(str1)
        len2 = len(str2)
        if str1.startswith(str2)==False:
            return ""

        for i in range(1,len2+1):#divede len2, i is duplicate times 
            if len2%i!=0:
                continue 
            sublen = len2//i
            if len1%sublen!= 0:
                continue
            substr = str2[0:sublen]
            if str2 != substr*i:
                continue
            else:
                if str1 == substr*(len1//sublen):
                    return substr
        return ""
#953. Verifying an Alien Dictionary		
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if(len(words)<=1):
            return True
       
        for i in range(1,len(words)):
            first = words[i-1]
            second = words[i]
            for j in range(len(first)):
                if j>= len(second) or order.index(second[j])<order.index(first[j]):#using str.index(ch)
                    return False
                elif order.index(second[j])>order.index(first[j]):
                    break
                """else:
                    continue"""
        return True
#encode and decode
def encode(s):
    ans = ""
    prec = ''
    cnt = 0
    for i in range(len(s)):
        if prec == '':
            prec = s[i]
        if s[i] == prec:
            cnt += 1
        else:
            ans += str(cnt) + prec
            prec = s[i]
            cnt = 1
    ans += str(cnt) + prec
    return ans

def decode(s):
    ans = ""
    for i in range(len(s)):
        if s[i].isdigit():
            cnt = int(s[i])
        else:
            ch = s[i]
            for j in range(cnt):
                ans += s[i]
    return ans
#28. Implement strStr()
##Approach1: 1 pointer and using substr
def strStr(self, haystack, needle):
	if needle == "":
		return 0
	q = 0
	sublen = len(needle)
	for p in range(len(haystack)):
		if haystack[p] == needle[q]:
			if haystack[p:p+sublen] == needle:
				return p
	return -1
##Approach2: 2 pointers, time cost is lower
 def strStr(self, haystack, needle):
	if needle == "":
		return 0
	p=0
	q = 0
	sublen = len(needle)
	while (p <len(haystack)) and (q < sublen):
		if haystack[p] == needle[q]:
			p += 1
			q += 1
		else:
			p = p+1-q#p back to the matched char next position
			q = 0
	if q == sublen:
		return p-sublen
	else:
		return -1
#383. Ransom Note
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
	letter = [0]*26
	for i in range(len(magazine)):
		ch = magazine[i]
		letter[ord(ch)-ord('a')] += 1
	for i in range(len(ransomNote)):
		ch = ransomNote[i]
		if letter[ord(ch)-ord('a')]<=0:
			return False
		letter[ord(ch)-ord('a')] -= 1
	return True
#557. Reverse Words in a String III
def reverseWords(self, s: str) -> str:
        str = s.split(" ")
        ans = ""
        for word in str:
            ans += word[::-1]+" "
        return ans.rstrip()
#696. Count Binary Substrings Time:O(n) space O(n)
def countBinarySubstrings(self, s: str) -> int:
	groups = []
	cnt = 1
	for i in range(1,len(s)):
		if s[i-1] != s[i]:
			groups.append(cnt)
			cnt = 1
		else:
			cnt += 1
	groups.append(cnt)#the last update should be added
	ans = 0
	for i in range(1,len(groups)):
		ans += min(groups[i-1],groups[i])
	return ans
#806. Number of Lines To Write String time  o(len(s)) space o(1)
  def numberOfLines(self, widths: List[int], s: str) -> List[int]:
	cnt = 1
	cur = 0
	for c in s:
		w = widths[ord(c)-ord('a')]
		cur += w
		if cur>100:
			cnt += 1
			cur = w
	return [cnt,cur]
#859. Buddy Strings
def buddyStrings(self, s: str, goal: str) -> bool:
	#add different pairs into list, list can be zero len or 2 len
	#len==0: there should be one char duplicated in string
	#len==2: pairs1=swap(pairs2)
	if len(s) != len(goal):
		return False
	pairs = []
	cnt = set()
	duplicate = False
	for i in range(len(s)):
		if s[i]!=goal[i]:
			pairs.append([s[i],goal[i]])
		if s[i] in cnt:
			duplicate = True
		else:
			cnt.add(s[i])
	if len(pairs) == 0:
		return duplicate
	if len(pairs)==2:
		if (pairs[0][0] == pairs[1][1]) and (pairs[0][1] == pairs[1][0]):
			return True
	return False	