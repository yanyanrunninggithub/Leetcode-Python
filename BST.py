#108. Convert Sorted Array to Binary Search Tree: using bs to create the BST
class Solution:
    def BSHelper(self,nums:List[int], start:int,end:int) -> TreeNode:
        if start > end:
            return None
        mid = start+(end-start)//2
        root = TreeNode(nums[mid])  #create new node
        root.left = self.BSHelper(nums,start,mid-1)
        root.right = self.BSHelper(nums,mid+1,end)
        return root
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.BSHelper(nums,0,len(nums)-1)
#235. Lowest Common Ancestor of a Binary Search Tree:  Time O(N)  
#Space Complexity: O(N)O(N). This is because the maximum amount of space utilized by the recursion stack would be NN since the height of a skewed BST could be NN. if improve space, no use recursion, traverse down the tree iteratively
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val <root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
#501. Find Mode in Binary Search Tree O(n) O(n)
class Solution:
    mode = []
    cnt = 0
    max_cnt = 0
    pre_val = 0
    def findMode(self, root: TreeNode) -> List[int]:
        self.inorder(root)
        return self.mode
    def inorder(self, root: TreeNode):
        if root == None:
            return
        self.inorder(root.left)
        self.visit(root)
        self.inorder(root.right)
    def visit(self,root: TreeNode):
        if root.val == self.pre_val:
            self.cnt += 1
        else:
            self.pre_val = root.val
            self.cnt = 1
        if self.cnt>self.max_cnt:
            self.max_cnt = self.cnt
            self.mode.clear()
        if self.cnt == self.max_cnt:
            self.mode.append(root.val)
#530. Minimum Absolute Difference in BST: time O(n)
class Solution:
    pre = None
    min_diff = float('inf')
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.inorder(root)
        return self.min_diff
    def inorder(self,root: TreeNode):
        if root == None:
            return
        self.inorder(root.left)
        if self.pre != None:
            self.min_diff = min(self.min_diff, abs(root.val-self.pre.val))
        self.pre = root
        self.inorder(root.right)
#653. Two Sum IV - Input is a BST  
#approach 1: for BST time O(n) space O(n)
def findTarget(self, root: TreeNode, k: int) -> bool:
	nodes = []
	def inorder(root: TreeNode):
		if root == None:
			return
		inorder(root.left)
		nodes.append(root.val)
		inorder(root.right)        
	inorder(root)
	#binary search in a sorted list
	p = 0
	q = len(nodes)-1
	while p<q:
		cur = nodes[p]+nodes[q]
		if cur == k:
			return True
		elif cur<k:
			p += 1
		else:
			q -= 1
	return False
#approach 2: for normal BT  Time O(n) space O(n)
def findTarget(self, root: TreeNode, k: int) -> bool:
	nodes = []  
	def find(root: TreeNode) -> bool:
		if root == None:
			return False
		if (k-root.val) in nodes:
			return True
		nodes.append(root.val)
		return find(root.left) or find(root.right)		   
	return find(root)
#938. Range Sum of BST
def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
	if root == None:
		return 0
	ans = 0
	if root.val<=high and root.val>=low:
		ans += root.val
	if root.val<=high:
		ans += self.rangeSumBST(root.right,low,high)
	if root.val>=low:
		ans += self.rangeSumBST(root.left,low,high)
	return ans