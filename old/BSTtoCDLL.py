class Node(object):
	"""docstring for Node"""
	def __init__(self, x):
		self.val = x
		self.leftpre = None
		self.rightnext = None
class Solution(object):
	"""docstring for Solution"""
	def mergeCDL(self, a, b):
		if not a: return b
		if not b: return a

		aEnd = a.leftpre
		bEnd = b.leftpre

		a.leftpre = bEnd
		bEnd.rightnext = a
		aEnd.rightnext = b
		b.leftpre = aEnd
		return a
	def BSTtoCDLL(self, root):
		if not root: return root
		left = self.BSTtoCDLL(root.leftpre)
		right = self.BSTtoCDLL(root.rightnext)
		root.leftpre =root
		root.rightnext = root

		head = self.mergeCDL(left, root)
		head = self.mergeCDL(head, right)
		return head
a = Node(10)
a.leftpre = Node(6)
a.leftpre.leftpre = Node(3)
a.leftpre.rightnext = Node(8)
a.rightnext = Node(20)
b = Solution()
c = b.BSTtoCDLL(a)
n = 0
while n < 20:
	print c.val
	c = c.rightnext
	n += 1
		