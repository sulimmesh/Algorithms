"""
Implementation of a tree data structure. Not necessarily a binary search
tree. 
"""
import collections
import copy

class TreeNode():
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.val)

	def __repr__(self):
		return str(self.val)

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

def bfs(q, target):
	if len(q) > 0:
		current_list = q.popleft()
		path = copy.copy(current_list[1])
		current = current_list[0]
		path.append(current)
		if current.val == target:
			return path
		if current.left:
			q.append([current.left,path])
		if current.right:
			q.append([current.right,path])
		return bfs(q, target)
	else:
		return None

def main():
	array = [1,2,3,4,5,6,7,8]
	root = buildTree(array)
	q = collections.deque()
	q.append([root,[]])
	target = 8
	print bfs(q, target)

if __name__ == "__main__":
	main()


