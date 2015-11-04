"""
Implementation of a tree data structure. Not necessarily a binary search
tree. 
"""
import collections

class TreeNode():
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def buildTree(vals):
	q = collections.deque()
	root = None
	cur = root
	for i in range(len(vals)):
		if not vals[i]:
			continue
		cur = TreeNode(vals[i])
		if i == 0:
			root = cur
		if len(q) > 0:
			parent = q.popleft()
			if parent.left:
				parent.right = cur
			else:
				parent.left = cur
		q.append(cur)
		q.append(cur)
	return root

def main():
	array = [1,2,3,None,4]
	root = buildTree(array)


if __name__ == "__main__":
	main()