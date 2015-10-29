"""
Main script for non-circular singly-linked list manipulation.
"""
class Node():
	def __init__(self, val=None):
		self.val = val
		self.prev = None
		self.next = None

def printList(head):
	while head:
		print head.val
		head = head.next

def build(vals):
	prev = None
	cur = Node()
	head = cur
	for i in range(len(vals)):
		if i == len(vals)-1:
			next = None
		else:
			next = Node()
		cur.val = vals[i]
		cur.prev = prev
		cur.next = next
		prev = cur
		cur = next
	return head

def reverse(cur):
	prev = None
	exit = False
	while cur:
		temp = cur.next
		cur.next = prev
		prev = cur
		cur = temp
	return prev

def removeFirst(head):
	temp = head.next
	return temp

def removeLast(head):
	cur = head
	while cur.next.next:
		cur = cur.next
	cur.next = None
	return head

def removeVal(head, val):
	cur = head
	if cur.val == val:
		return removeFirst(cur)
	while cur:
		if cur.next:
			if cur.next.val == val:
				cur.next = cur.next.next
		cur = cur.next
	return head

def insertFirst(head, val):
	new_node = Node(val)
	new_node.next = head
	return new_node

def insertLast(head, val):
	new_node = Node(val)
	cur = head
	while cur.next:
		cur = cur.next
	cur.next = new_node
	return head

def insertAtK(head, val, k):
	if k <= 1:
		return insertFirst(head, val)
	count = 2
	cur = head
	while cur:
		if count == k:
			temp = cur.next
			cur.next = Node(val)
			cur.next.next = temp
		cur = cur.next
		count += 1
	if k >= count:
		return insertLast(head, val)
	return head

def main():
	vals = [1,2,3,4,5,6,7,8,9,10]
	#build list
	head = build(vals)
	printList(head)
	print
	#reverse list
	reverse_head = reverse(head)
	printList(reverse_head)
	print
	head = reverse(reverse_head)
	#remove first node
	head = removeFirst(head)
	printList(head)
	print
	#remove last node
	head = removeLast(head)
	printList(head)
	print
	#remove value 5
	head = removeVal(head, 5)
	printList(head)
	print
	#insert 5 first
	head = insertFirst(head, 5)
	printList(head)
	print
	#insert 5 last
	head = insertLast(head, 5)
	printList(head)
	print
	#insert 10 at the 3rd position
	head = insertAtK(head, 10, 3)
	printList(head)

if __name__ == "__main__":
	main()