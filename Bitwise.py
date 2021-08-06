 #461. Hamming Distance
 def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        while x!=0 or y!=0:
            if (x&1) != (y&1):
                cnt += 1
            x = x>>1
            y = y>>1
        return cnt
 def hammingDistance(self, x: int, y: int) -> int:
        xx = []
        yy = []
        while x!=0:
            xx.append(x&1)
            x = x>>1
        while y!=0:
            yy.append(y&1)
            y = y>>1
        i=0
        cnt = 0
        while i<len(xx) and i<len(yy):
            if xx[i]!= yy[i]:
                cnt += 1
            i += 1
        while i<len(xx):
            if xx[i] == 1:
                cnt += 1
            i += 1
        while i<len(yy):
            if yy[i] == 1:
                cnt += 1
            i += 1
        return cnt
#476. Number Complement
def findComplement(self, num: int) -> int:
	nums = []
	while num!=0:
		nums.append(num&1)
		num = num>>1
	ans = 0
	for i in range(len(nums)-1,-1,-1):#reverse nums list scan
		ans = (ans<<1) + abs(nums[i]-1)
	return ans
#1009. Complement of Base 10 Integer
def bitwiseComplement(self, n: int) -> int:
	if n==0:
		return 1
	ans = 0
	cnt = 0
	while n>0:
		digit = 1-(n&1)
		ans += (2**cnt)*digit
		cnt += 1
		n = n>>1
	return ans
#1018. Binary Prefix Divisible By 5: time O(N) space O(N)
def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
	ans = [False]*len(nums)
	num = 0
	for i in range(len(nums)):
		num = ((num<<1)+nums[i])
		if num%5 == 0:
			ans[i] = True
	return ans