# class Solution(object):
# 	def majorityElement(self, nums):
# 		majDict = {}
# 		for x in nums:
# 			if (majDict.has_key(x)):
# 				val = majDict.get(x)
# 				if val + 1 > len(nums)/2:
# 					return x
# 				majDict[x] = val + 1
# 			else: 
# 				majDict[x] = 1
# 				if 1 > len(nums)/2:
# 					return x
# 		return -1

# a = [1,2]
# s = Solution()
# print s.majorityElement(a)


# b = [1,2]
# print b
# d = b[-1:]
# c = b[:len(b)-1] 
# b = d+c
# print b


grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
row = len(grid)
print row
col = len(grid[0])
p = 0
for r, row in enumerate(grid):
	for c, val in enumerate(row):
		if val == 1: 
			print 'row = ', r, 'col = ', c
			neber = 0
			if 0 <= r-1 and grid[r-1][c] == 1: neber += 1
			# if r+1 < row and grid[r+1][c] == 1: neber += 1
			if 0 <= c-1 and grid[r][c-1] == 1: neber += 1
			if c+1 < col and grid[r][c+1] == 1: neber += 1
			p = p + 4 - neber
			print 'p = ', p