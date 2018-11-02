class solution(object):
	def sorted(self, nums):
		if not nums: return []
		p = 0
		res = []
		for i, x in enumerate(nums):
			if x < 0:
				p = i
		q = p + 1
		while -1 < p and q < len(nums):
			res.append(min(nums[p]**2,nums[q]**2))
			res.append(max(nums[p]**2,nums[q]**2))
			p -= 1
			q += 1
		while -1 < p:
			res.append(nums[p]**2)
			p -= 1 
		while q < len(nums):
			res.append(nums[q]**2)
			q += 1
		return res
nums = [-3, -2, -1, 0, 1,2,3,4,5]
# nums = [-3, -2, -1]
# nums = [1,2,3,4,5]
a = solution()
print a.sorted(nums)  