#20. Valid Parentheses
class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            else:
                if len(stack)<=0:  #"()]"
                    return False
                else:
                    if s[i] == ')':
                        if stack.pop() != '(':
                            return False
                    if s[i] == ']':
                        if stack.pop() != '[':
                            return False 
                    if s[i] == '}':
                        if stack.pop() != '{':
                            return False
        return True if len(stack)==0 else False  #"((("
#1021. Remove Outermost Parentheses: time O(n) space O(n)
 def removeOuterParentheses(self, s: str) -> str:
	stack = []
	ans = ""
	cnt1, cnt2 = 0, 0
	for ch in s:
		if ch == '(':
			stack.append(ch)
			cnt1 += 1
		else:
			stack.append(ch)
			cnt2 += 1
		if cnt1 == cnt2:
			stack.pop(0)
			stack.pop(-1)
			for c in stack:
				ans += c
			stack.clear()
			cnt1 = 0
			cnt2 = 0
	return ans
#232. Implement Queue using Stacks
class MyQueue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:  #o(1)
        self.s1.append(x)

    def pop(self) -> int:             #o(n)
        if(len(self.s2) == 0):
            while len(self.s1)!=0:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if(len(self.s2) == 0):
            while len(self.s1)!=0:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        if len(self.s1) == 0 and len(self.s2) == 0:
            return True
        return False
#1047. Remove All Adjacent Duplicates In String： timeO（n) spaceO(n)
def removeDuplicates(self, s: str) -> str:
	ans = []
	for ch in s:
		if len(ans) == 0:
			ans.append(ch)
		else:
			if ch!=ans[-1]:
				ans.append(ch)
			else:
				ans.pop()
	return "".join(ans)
	return "".join(ans)