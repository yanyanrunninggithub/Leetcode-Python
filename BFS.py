#637. Average of Levels in Binary Tree
#Time complexity : O(n). The whole tree is traversed atmost once
#Space complexity : O(m)O(m). Here, mm refers to the maximum mumber of nodes at any level in the input tree.
def averageOfLevels(self, root: TreeNode) -> List[float]:
	ans = []
	queue = []
	queue.append(root)
	while len(queue) != 0:
		sum = 0
		cnt = 0
		tmp = []
		while len(queue) != 0:
			node = queue.pop(0)
			sum += node.val
			cnt += 1
			if node.left != None:
				tmp.append(node.left)
			if node.right != None:
				tmp.append(node.right)
		queue = tmp
		ans.append(sum/cnt)
	return ans