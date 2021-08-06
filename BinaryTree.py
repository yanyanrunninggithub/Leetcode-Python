class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))  #creating tree

#104. Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None: # this return condition can be removed, not impact the result
            return 1
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
#minimum depth of BS
def minDepth(root:TreeNode) -> int:
	depth = 0
	queue = []
	queue.append(root)
	while len(queue)>0:
		depth += 1
		node = queue.pop(0)
		if node.left == None and node.right == None: #the first leaf we meet its depth is min
			return depth
		if node.left != None:
			queue.append(node.left)
		else:
			queue.append(node.right)
#543. Diameter of Binary Tree
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    ans = 0#global value
    def diameterOfBinaryTree(self, root):
        def getHeight(root):#child function can without self argument
            if root == None:
                return 0
            l = getHeight(root.left)
            r = getHeight(root.right)
            self.ans = max(self.ans,l+r)#global value must use self.
            return 1+max(l,r)#return tree height
        if root == None:
            return 0
        getHeight(root)
        return self.ans
		
class Solution(object):
    ans = 0
    def getHeight(self, root):#all functions in class should add self argument
        if root is None:
            return 0
        l = self.getHeight(root.left)#call object function
        r = self.getHeight(root.right)
        self.ans = max(self.ans,l+r)
        return 1+max(l,r)
    
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        self.getHeight(root)
        return self.ans
#993. Cousins in Binary Tree
class Solution(object):
    def isCousins(self, root, x, y):
        x_parent = None
        y_parent = None
        x_depth = 0
        y_depth = 0
        def pre_order(root,x,y,preNode,depth):
            if root == None:
                return
            if root.val == x:
                x_parent = preNode
                x_depth = depth
            if root.val == y:
                y_parent = preNode
                y_depth = depth
            pre_order(root.right,x,y,root,depth+1)#each recursion call a updated parent and depth++
            pre_order(root.left,x,y,root,depth+1)
            
        pre_order(root,x,y,None,0)
        return (x_parent!=y_parent) and (x_depth==y_depth)#parent different but depth same
#94. Binary Tree Inorder Traversal
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        ans = []
        if root == None:
            return ans
        if root.left != None:
            ans += self.inorderTraversal(root.left)#list add list using +
        ans.append(root.val)
        if root.right != None:
            ans += self.inorderTraversal(root.right)
        return ans	
#100. Same Tree   #very similar to 101.symmetric Tree
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)		

#get BT leaves
def getLeaf(root:TreeNode) -> list:
    leaf = [] #list initial before return situation
    if root == None:
        return leaf
    if root.left == None and root.right == None:
        leaf.append(root.val)
    leaf += getLeaf(root.left)
    leaf += getLeaf(root.right)
    return leaf
#404. Sum of Left Leaves
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        sum = 0 #val initial after return situation
        if root.left != None and root.left.left == None and root.left.right == None: #if is left leaf
            sum += root.left.val
        sum += self.sumOfLeftLeaves(root.left)
        sum += self.sumOfLeftLeaves(root.right)
        return sum
#563. Binary Tree Tilt   
#Time Complexity: O(N)  We traverse each node once and only once.
#Space Complexity: O(N) the variables are constant-size, but recursion in the algorithm which incurs additional memory consumption in function call stack.
class Solution:
    total = 0
    def findTilt(self, root: TreeNode) -> int:        
        def sumValue(root): #sub-function
            if root == None:
                return 0
            left = sumValue(root.left)
            right = sumValue(root.right)
            self.total += abs(right-left)
            return left+right+root.val
        sumValue(root)
        return self.total
#606. Construct String from Binary Tree Time O(n) space O(n) for recursion
 def tree2str(self, root: TreeNode) -> str:
	if root == None:
		return ""
	if root.left == None and root.right == None:
		return str(root.val)+""
	if root.right == None:
		return str(root.val)+"("+self.tree2str(root.left)+")"
	return str(root.val)+"("+self.tree2str(root.left)+")("+self.tree2str(root.right)+")"
#617. Merge Two Binary Trees
#time O(M) M represents the minimum number of nodes from the two given trees.
#space O(M) The depth of the recursion tree can go upto m in the case of a skewed tree. In average case, depth will be O(logm)O(logm).
def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
	if root1 == None:
		return root2
	if root2 == None:
		return root1
	root1.val += root2.val
	root1.left = self.mergeTrees(root1.left,root2.left)
	root1.right = self.mergeTrees(root1.right,root2.right)
	return root1
#1022. Sum of Root To Leaf Binary Numbers 
#time O(n) space up to O(H) to keep the recursion stack, where HH is a tree height.
class Solution:
    ans = 0
    def preorder(self,root: TreeNode,num: int):           
        if root == None:
            return
        num = (num<<1) + root.val
        if root.left == None and root.right == None:
            self.ans += num
        self.preorder(root.left,num)
        self.preorder(root.right,num)
        return self.ans
    def sumRootToLeaf(self, root: TreeNode) -> int:        
        self.preorder(root,0)
        return self.ans