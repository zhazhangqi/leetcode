class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class solution():
	def he(self,nums,h,l):
	    if h < l: return None
	    m = (h + l) / 2
	    x = TreeNode(nums[m])
	    x.left = self.he(nums,m-1,l)
	    x.right = self.he(nums,h,m+1)
	    return x

nums = [1,2,3,4,5,6,7,8,9]
s = solution()
x = s.he(nums,len(nums)-1,0)
y = [x]
while y:
	q = y.pop(0)
	print q.val
	if q.left: y.append(q.left)
	if q.right: y.append(q.right)